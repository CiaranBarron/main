<!DOCTYPE html>
<html>
  <head>

    <meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
    <link rel="stylesheet" type="text/css" href="../static/mainstyle.css">
    <script src="../static/scripts.js"></script>
    <script async defer src="https://maps.googleapis.com/maps/api/js?key=AIzaSyD_A2XKU-wVSr9dGPoYBxir0vI2ieENbCo&callback=initMap"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>

  </head>

  <body>

      <!-- Header -->
      <header id="headerbox">
        <h1 style="margin-bottom: 0">
          Dublin Bikes
        </h1>
        <hr style="width: 20%">
        <p>
          Realtime Information
        </p>
      </header>

      <!-- Main Body: Map and interactive info window -->
      <div id="contentwindow">
        <div id="map"></div>
          <div id="infobox">

            <div class="dropdown">
              <button class="dropbtn" >Dropdown</button>
              <div class="dropdown-content">
                <a href="#" onclick="clickHandler(1)">Close</a>
                <a href="#" onclick="clickHandler(2)">Find Station</a>
                <a href="#" onclick="clickHandler(3)">Forecast Centre</a>
              </div><br>
            </div><br>

            <div id="infoboxcontent">
              <h2 id="station">Dublin Bikes</h2>
              <hr style="width: 40%">
              <h3>Status</h3>
              <p>Open/Closed</p>
              <hr style="width: 30%">
              <h3 style= "display: inline-block; margin-bottom: 0;">Available  Bikes:</h3>
              <p id ="avbikes" style= "display: inline-block; margin-bottom: 0;">Loading...</p>
              <br>
              <h3 style= "display: inline-block; margin-top: 0;">Available Stands:</h3>
              <p id ="avstands" style= "display: inline-block; margin-bottom: 0;">Loading...</p>
              <hr style="width: 30%">
              <h3 style ="margin-bottom: 10px;">Weather</h3>
              <img src="../static/images/sunnyicon.png" alt="Sunny" style="width:50px;height:50px;">
              <hr style="width: 10%">
            </div>
        </div>
      </div>

      <!-- Footer -->
      <footer id=footerbox>
        <h3>Dublin Bikes</h3>
      </footer>

  </body>
</html>
