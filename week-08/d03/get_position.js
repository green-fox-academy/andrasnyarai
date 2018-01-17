'use strict'
    
var city = ''
    
let input = document.querySelector('input')
let button = document.querySelector('button:first-of-type')

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
    googleFrame.dataset.place = place
    googleFrame.dataset.street = 'https://www.google.com/maps/embed/v1/streetview?key=AIzaSyAHgL__l8gyDDHITQjT-p8uBFsHVZjJDLc&location=' + lat + ','+ lon
    
    newButton.addEventListener('click', function() {
        let status = true
        if (!view && status) {
            googleFrame.setAttribute('src', googleFrame.dataset.street )
            view = true
            status = false          
        } else if (view && status) {
            googleFrame.setAttribute('src', googleFrame.dataset.place )
            view = false         
            status = false          
        }
    })
}).fail(function(err) {
    throw err;
});
}

let newButton = document.createElement('button')
newButton.textContent = 'VIEW'
document.querySelector('body').appendChild(newButton)

let view = false