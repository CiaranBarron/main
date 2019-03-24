'''
Created on 12 Feb 2019

@author: Ciaran Barron

Retrieve data from DublinBikes API and store in Amazon RDS DB
'''

import sqlalchemy as sqla
import requests as req
import pandas as pd
import time
import json

with open('D:/College/S2/COMP30830/Project/authentication.txt') as f:
    auth=f.read().split('\n')
    
Key=auth[0]
Contract=auth[1]
URL =auth[2]
LOG =auth[3]
PWD =auth[4]
DB  =auth[5]
TAB =auth[6]
PORT=auth[7]
WKEY=auth[8]

ENG ="mysql+mysqldb://{0}:{1}@{2}:{3}/{4}".format(LOG,PWD,URL,PORT,DB)

engine = sqla.create_engine(ENG,echo=False)

def scrape_dynamic_data():
    
    response = req.get('https://api.jcdecaux.com/vls/v1/stations?contract={0}&apiKey={1}'.format(Contract,Key))
    Data = pd.DataFrame(response.json())
    
    available_bike_stands = Data['available_bike_stands']
    available_bikes = Data['available_bikes']
    bike_stands = Data['bike_stands']
    last_update = Data['last_update']
    number = Data['number']
    status = Data['status']
    
    for i in range(Data.shape[0]):

        SQL = """
        INSERT INTO {0}.{1} (available_bike_stands,
                   available_bikes,
                   bike_stands,
                   last_update,
                   number,
                   status)
        VALUES ({2}, {3}, {4}, {5}, {6}, \"{7}\")
        """.format(
            DB,
            TAB,
            available_bike_stands[i],
            available_bikes[i],
            bike_stands[i],
            last_update[i],
            number[i],
            status[i])

        try: 
            engine.execute(SQL)

        except:
            pass
        
        #calling weather scraper
        scrape_weather_data(number[i], i)

# Function for scraping weather information that is relevant         
def scrape_weather_data(TIME,i):
    
    static_data = pd.read_sql_table('static', engine)

    Latitude = static_data['latitude'][i]
    Longitude= static_data['longitude'][i]
    
    weather_url = "https://api.darksky.net/forecast/{}/{},{},{}".format(
        WKEY,
        Latitude,
        Longitude,
        TIME)
    
    weatherjson = req.get(weather_url)

    print(weatherjson.json())
    # no need to read_json as format is dictionary like already.
    weather = pd.DataFrame(weatherjson.json())
    
#     print(weather['currently'])
#     print(weather['flags'])
#     print(weather['offset'])
    
def continuous_scrape():
    
    while True:
        
        #scrape data and write to RDS DB
        scrape_dynamic_data()

        # Print update message
        dtime=time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print('Data written to DublinBikesDB.dynamic at {0}'.format(dtime))

        # sleep for 1 minute
        time.sleep(60)

if __name__ == '__main__':
    
    # continuous_scrape()
    scrape_dynamic_data()
    
    