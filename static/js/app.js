

const pythonUrl = "/anamolies";

function createMap(rng_1880_1910_layer,
                   rng_1911_1940_layer,
                   rng_1941_1970_layer,
                   rng_1971_2000_layer,
                   rng_2001_2017_layer) {

  // Create the tile layer that will be the background of our map
  var lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/light-v9/tiles/256/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"http://openstreetmap.org\">OpenStreetMap</a> contributors, <a href=\"http://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"http://mapbox.com\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.streets",
    accessToken: API_KEY
  });

  // Create a baseMaps object to hold the lightmap layer
  var baseMaps = {
    "Light Map": lightmap
  };

  // Create an overlayMaps object to hold the bikeStations layer
  var overlayMaps = {
    
    "1880-1910": rng_1880_1910_layer,
    "1911-1940": rng_1911_1940_layer,
    "1941-1970": rng_1941_1970_layer,
    "1971-2000": rng_1971_2000_layer,
    "2001-2017": rng_2001_2017_layer
  };

  // Create the map object with options
  var myMap = L.map("map", {
    center: [0, 0],
    zoom: 3,
    layers: [lightmap, 
            rng_1880_1910_layer,
            rng_1911_1940_layer,
            rng_1941_1970_layer,
            rng_1971_2000_layer,
            rng_2001_2017_layer]
  });

  // Create a layer control, pass in the baseMaps and overlayMaps. Add the layer control to the map
  L.control.layers(baseMaps, overlayMaps, {
    collapsed: false
  }).addTo(myMap);
}

function tempColor(temp) {
  switch (true) {
  case (temp > -15.0 && temp <= -2.0):
    return "blue";
  case temp > -2 && temp < 4.0:
    return "yellow";
  case temp >= 4.0 && temp < 10.0:
    return "orange";  
  case temp >= 10.0:
    return "red";    
  default:
    return "black";
  }
}


function createCircles() {
  
    d3.json(pythonUrl).then(function(data) {
    
    pythonData = data[0];

    var rng_1880_1910_array = [];
    var rng_1911_1940_array = [];
    var rng_1941_1970_array = [];
    var rng_1971_2000_array = [];
    var rng_2001_2017_array = [];

    for (var i=0; i < pythonData['City'].length; i++) {
   
      var Lat = pythonData['Lat'][i];
      var Lng = pythonData['Lng'][i];
      var city = pythonData['City'][i];
      var country = pythonData['Country'][i];
      var rng_1880_1910 = pythonData['rng_1880_1910'][i];
      var rng_1911_1940 = pythonData['rng_1911_1940'][i];
      var rng_1941_1970 = pythonData['rng_1941_1970'][i];
      var rng_1971_2000 = pythonData['rng_1971_2000'][i];
      var rng_2001_2017 = pythonData['rng_2001_2017'][i];

      var rng_1880_1910_marker = L.circle([Lat,Lng], {
            fillOpacity: 0.75,
            color: tempColor(rng_1880_1910),
            
            radius: rng_1880_1910*-2000})
            .bindPopup("<h1>Country:" + country + "</h1> <hr> <h3>1880-1910: " + rng_1880_1910 + "</h3>");

      var rng_1911_1940_marker = L.circle([Lat,Lng], {
            fillOpacity: 0.75,
            color:tempColor(rng_1911_1940),
           
            radius: rng_1911_1940*7000})
            .bindPopup("<h1>Country:" + country + "</h1> <hr> <h3>1911-1940: " + rng_1911_1940 + "</h3>");

      var rng_1941_1970_marker = L.circle([Lat,Lng], {
          fillOpacity: 0.75,
          color: tempColor(rng_1941_1970),
         
          radius: rng_1941_1970*10000})
          .bindPopup("<h1>Country:" + country + "</h1> <hr> <h3>1941-1970: " + rng_1941_1970 + "</h3>");

      var rng_1971_2000_marker = L.circle([Lat,Lng], {
          fillOpacity: 0.75,
          color:tempColor(rng_1971_2000),
          
          radius: rng_1971_2000*10000})
          .bindPopup("<h1>Country:" + country + "</h1> <hr> <h3>1971-2000: " + rng_1971_2000 + "</h3>");

      var rng_2001_2017_marker = L.circle([Lat,Lng], {
          fillOpacity: 0.75,
          color:tempColor(rng_2001_2017),
          
          radius: rng_2001_2017*10000})
          .bindPopup("<h1>Country:" + country + "</h1> <hr> <h3>2001-2017: " + rng_2001_2017 + "</h3>");

      
    rng_1880_1910_array.push(rng_1880_1910_marker);
    rng_1911_1940_array.push(rng_1911_1940_marker);
    rng_1941_1970_array.push(rng_1941_1970_marker);
    rng_1971_2000_array.push(rng_1971_2000_marker);
    rng_2001_2017_array.push(rng_2001_2017_marker);

   
  }//for loop end

  
  var rng_1880_1910_layer = L.layerGroup(rng_1880_1910_array);
  var rng_1911_1940_layer = L.layerGroup(rng_1911_1940_array);
  var rng_1941_1970_layer = L.layerGroup(rng_1941_1970_array);
  var rng_1971_2000_layer = L.layerGroup(rng_1971_2000_array);
  var rng_2001_2017_layer = L.layerGroup(rng_2001_2017_array);

  
  createMap(
    rng_1880_1910_layer,
    rng_1911_1940_layer,
    rng_1941_1970_layer,
    rng_1971_2000_layer,
    rng_2001_2017_layer
  ); 

});//d3.json end
    

  
};//get circles end




createCircles();