// Creating map object
var myMap = L.map("map", {
    center: [0, 0],
    zoom: 5
  });

  // Adding tile layer to the map
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 11,
    id: "mapbox.streets",
    accessToken: API_KEY
  }).addTo(myMap);


var dataset = []
d3.csv('cities_lat_lgn.csv', function(data) {
   var dataset = data.map(function(d) { return d});
   
//    console.log(dataset[0])

   for (var i = 0 ; i < dataset.length; i++){

        var lat = dataset[i].Lat;
        var lng = dataset[i].Lng;
        var city = dataset[i].City;
        var country = dataset[i].Country;


        console.log(city);
        console.log('country',country);

        L.circle([lat,lng], {
            fillOpacity: 0.75,
            color:'red',
            fillColor: 'red',
            radius: 10000
        }).bindPopup("<h1>" + city + "</h1> <hr> <h3>Magnitude: " + country + "</h3>")
          .addTo(myMap);
  

   };




})