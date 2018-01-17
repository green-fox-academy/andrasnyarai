'use strict'

let httpRequest = new XMLHttpRequest();
httpRequest.open('GET', 'http://api.giphy.com/v1/gifs/search?q=funny+cute&api_key=8qBC6DxDTPsmGINpS5oDrCgatDxDKZen', true); // Also try http://444.hu/feed
httpRequest.send(null);
httpRequest.onreadystatechange = console.log;
httpRequest.onload = function() {
    var images = JSON.parse(httpRequest.responseText);
    for (let i = 0; i < images.data.length; i++) {
        let theBody = document.querySelector('body')
        let imgContainer = document.createElement('img')
        imgContainer.setAttribute('src', images.data[i].images.downsized_still.url)
        imgContainer.dataset.gif = images.data[i].images.downsized.url
        imgContainer.addEventListener('click', function () {
            imgContainer.setAttribute('src', imgContainer.dataset.gif)
            
        })
        theBody.appendChild(imgContainer)
    }
    console.log(images.data[0])
}