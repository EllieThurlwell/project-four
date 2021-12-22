var map;
var labels;
var locations;
var markers;
var markerClusterer;

function initMap() {
   map = new google.maps.Map(document.getElementById('map'), {
      center: {
         lat: 41.384269489224444,
         lng: 2.1762469960733286
      },
      zoom: 11
   });

   labels = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';

   locations = [
       { lat: 41.37492, lng: 2.1888 },
       { lat:41.37116, lng:2.15174 },
       { lat:41.38812, lng:2.18601 }
   ];

   markers = locations.map(function(location, i) {
       return new google.maps.Marker({
           position: location,
           label: labels[i % labels.length]
       });
   });

   markerClusterer = new MarkerClusterer(map, markers, {imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'});
}