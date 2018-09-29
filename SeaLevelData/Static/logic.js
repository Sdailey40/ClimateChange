// Function to determine marker size based on population

//function markerSize(population) {
 // return population;
//}

// An array containing all of the information needed to create city and state markers
//var locations = 


// Define arrays to hold created city and state markers
//var cityMarkers = [];
//var stateMarkers = [];

// Loop through locations and create city and state markers
//for (var i = 0; i < locations.length; i++) {
  // Setting the marker radius for the state by passing population into the markerSize function
  //stateMarkers.push(
  //  L.circle(locations[i].coordinates, {
  //    stroke: false,
  //    fillOpacity: 0.75,
  //    color: "white",
  //    fillColor: "white",
  //    radius: markerSize(locations[i].state.population)
  //  })
  //);

  // Setting the marker radius for the city by passing population into the markerSize function
  //cityMarkers.push(
  //  L.circle(locations[i].coordinates, {
  //    stroke: false,
  //    fillOpacity: 0.75,
  //    color: "purple",
  //    fillColor: "purple",
  //    radius: markerSize(locations[i].city.population)
  //  })
  //);
//}
function getPins() {
  bounds = maps.getBounds();
  url = "mongodb://localhost:27017/Dion_db" + bounds.get().latitude + "longitude" + bounds.get().longitude
  $.get (url, pinTheMap, "json")
}

function pinTheMap(data) {
  map.removelayer(MarkerLayerGroup);

  var markerArray = new Array (data.length)
  for (var i = 0; i < data.length; i++){
        park = data [i];
        markerArray [i] = L.marker([park.pos[1], park.pos[0]]).bindPopup(park.Name);
  }

        markerLayerGroup = L.LayerGroup(markerArray).addTO(map);

  

// Create two separate layer groups: one for cities and one for states
//var states = L.layerGroup(stateMarkers);
//var cities = L.layerGroup(cityMarkers);


map.on('dragend', getPins);
map.on('zoomend', getPins);
map.whenReady(getPins)
// Create a baseMaps object
//var baseMaps = {
//  "Street Map": streetmap,
//  "Dark Map": darkmap
//};

// Create an overlay object
//var overlayMaps = {
 // "State Population": states,
  //"City Population": cities
};

// Define variables for our base layers
var streetmap = L.tileLayer({
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
});

var darkmap = L.tileLayer({
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.dark",
  accessToken: API_KEY
});

// Define a map object
var myMap = L.map("map", {
  center: [37.09, -95.71],
  zoom: 5,
  //layers: [streetmap, states, cities]
  layers: [streetmap]
});

// Pass our map layers into our layer control
// Add the layer control to the map
//L.control.layers(baseMaps, overlayMaps, {
//  collapsed: false
//}).addTo(myMap);
