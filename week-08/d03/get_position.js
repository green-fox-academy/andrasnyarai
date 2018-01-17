'use strict'
    
var city = ''
    
let input = document.querySelector('input')
let button = document.querySelector('button')

button.addEventListener('click', function () {
    city = input.value
    console.log(city)
    call()
})     

function call () {

    var url = "https://devru-latitude-longitude-find-v1.p.mashape.com/latlon.php?location=" + city;

    $.ajax({
      url: url,
      method: 'GET',
      headers: {
        "X-Mashape-Key": "kD0uEpXfdLmshbBtzPxApb2C0lWAp1SYQo9jsn5BqjtXfvh4bu",
        "Accept": "application/json"
      }
    }).done(function(result) {
    
    console.log(result.Results)

    var lon = result.Results[0].lon
    var lat = result.Results[0].lat

    let googleFrame = document.querySelector('iframe')
    let place = 'https://www.google.com/maps/embed/v1/place?key=AIzaSyAHgL__l8gyDDHITQjT-p8uBFsHVZjJDLc&q=' + lat + ','+ lon
    googleFrame.setAttribute('src', place )
    
    }).fail(function(err) {
        throw err;
      });
}