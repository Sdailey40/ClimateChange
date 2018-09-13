

function createMap(city_layer,
                    rng_1880_1910_layer,
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
    "Climate City": city_layer,
    "1880-1910": rng_1880_1910_layer,
    "1911-1940": rng_1911_1940_layer,
    "1941-1970": rng_1941_1970_layer,
    "1971-2000": rng_1971_2000_layer,
    "2001-2017": rng_2001_2017_layer
  };

  // Create the map object with options
  var myMap = L.map("map", {
    center: [0, 0],
    zoom: 5,
    layers: [lightmap, 
             city_layer, 
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

function createCircles(data) {

  var dataset = data.map(function(d) { return d});

  var city_array = [];
  var rng_1880_1910_array = [];
  var rng_1911_1940_array = [];
  var rng_1941_1970_array = [];
  var rng_1971_2000_array = [];
  var rng_2001_2017_array = [];
  
  for (var i = 0 ; i < dataset.length; i++){

        var Lat = dataset[i].Lat;
        var Lng = dataset[i].Lng;
        var city = dataset[i].City;
        var country = dataset[i].Country;
        var rng_1880_1910 = dataset[i].rng_1880_1910;
        var rng_1911_1940 = dataset[i].rng_1911_1940;
        var rng_1941_1970 = dataset[i].rng_1941_1970;
        var rng_1971_2000 = dataset[i].rng_1971_2000;
        var rng_2001_2017 = dataset[i].rng_2001_2017;

        var city_circle_marker =  L.circle([Lat,Lng], {
            fillOpacity: 0.75,
            color:'red',
            fillColor: 'red',
            radius: 10000})
            .bindPopup("<h1>City:" + city + "</h1> <hr> <h3>Country: " + country + "</h3>");

        var rng_1880_1910_marker = L.circle([Lat,Lng], {
            fillOpacity: 0.75,
            color:'blue',
            fillColor: 'blue',
            radius: rng_1880_1910*10000})
            .bindPopup("<h1>City:" + city + "</h1> <hr> <h3>Country: " + country + "</h3>");

        var rng_1911_1940_marker = L.circle([Lat,Lng], {
            fillOpacity: 0.75,
            color:'blue',
            fillColor: 'blue',
            radius: rng_1911_1940*10000})
            .bindPopup("<h1>City:" + city + "</h1> <hr> <h3>Country: " + country + "</h3>");

        var rng_1941_1970_marker = L.circle([Lat,Lng], {
          fillOpacity: 0.75,
          color:'blue',
          fillColor: 'blue',
          radius: rng_1941_1970*10000})
          .bindPopup("<h1>City:" + city + "</h1> <hr> <h3>Country: " + country + "</h3>");

        var rng_1971_2000_marker = L.circle([Lat,Lng], {
          fillOpacity: 0.75,
          color:'blue',
          fillColor: 'blue',
          radius: rng_1971_2000*10000})
          .bindPopup("<h1>City:" + city + "</h1> <hr> <h3>Country: " + country + "</h3>");

        var rng_2001_2017_marker = L.circle([Lat,Lng], {
          fillOpacity: 0.75,
          color:'blue',
          fillColor: 'blue',
          radius: rng_2001_2017*10000})
          .bindPopup("<h1>City:" + city + "</h1> <hr> <h3>Country: " + country + "</h3>");

      city_array.push(city_circle_marker);
      rng_1880_1910_array.push(rng_1880_1910_marker);
      rng_1911_1940_array.push(rng_1911_1940_marker);
      rng_1941_1970_array.push(rng_1941_1970_marker);
      rng_1971_2000_array.push(rng_1971_2000_marker);
      rng_2001_2017_array.push(rng_2001_2017_marker);

    }

   
  city_layer = L.layerGroup(city_array);
  rng_1880_1910_layer = L.layerGroup(rng_1880_1910_array);
  rng_1911_1940_layer = L.layerGroup(rng_1911_1940_array);
  rng_1941_1970_layer = L.layerGroup(rng_1941_1970_array);
  rng_1971_2000_layer = L.layerGroup(rng_1971_2000_array);
  rng_2001_2017_layer = L.layerGroup(rng_2001_2017_array);

  createMap(city_layer,
            rng_1880_1910_layer,
            rng_1911_1940_layer,
            rng_1941_1970_layer,
            rng_1971_2000_layer,
            rng_2001_2017_layer
          );
  
}


d3.csv('climate_by_city.csv',createCircles);