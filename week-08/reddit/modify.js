'use strict'

var id;

function validify () {

    let submitArea = document.querySelector('#submit').value.trim()
    let textAreaContent = document.querySelector('#textarea').value.trim()
    
    if (submitArea.length > 0 && textAreaContent.length > 0) {
        modify(submitArea, textAreaContent)
    } else {
        alert('You provided no subjects!')
    }
}

function modify(title, url) {
    
    let httpRequest = new XMLHttpRequest();
    // httpRequest.open('POST', 'http://secure-reddit.herokuapp.com/simple/posts', true);
    httpRequest.open('PUT', 'https://time-radish.glitch.me/posts/'+id, true);
    
    httpRequest.setRequestHeader("Accept", "application/json");
    httpRequest.setRequestHeader("Content-Type", "application/json");
    httpRequest.setRequestHeader("Username", "Andris");

    let params = {
        "title": title,
        "url": url,
      }
    
    httpRequest.onreadystatechange = console.log
    httpRequest.onreadystatechange = function() {

        if(httpRequest.readyState == 4 && httpRequest.status == 200) {
            window.location.replace("file:///C:/Users/Andras/greenfox/andrasnyarai/week-08/reddit/index.html");
        }
    }
    console.log(JSON.stringify(params))
    httpRequest.send(JSON.stringify(params));
    
}

var nbspFix = document.querySelector('.form');
nbspFix.innerHTML = nbspFix.innerHTML.replace(/&nbsp;/g,'');

let button = document.querySelector('.button')
button.addEventListener('click', validify)

let fillData = window.location.href.split('para')

let newUrl = decodeURIComponent(fillData[1]).split('')
newUrl.splice(0,2)
newUrl.splice(newUrl.length - 1, 1)
newUrl = newUrl.join('')

let newTitle = decodeURIComponent(fillData[2]).split('')
newTitle.splice(0,2)
newTitle.splice(newTitle.length - 1, 1)
newTitle = newTitle.join('')

let newId = decodeURIComponent(fillData[3]).split('')
newId.splice(0,1)
newId = newId.join('')
id = newId

document.querySelector('.form > #submit').value = newTitle
document.querySelector('.form > #textarea').value = newUrl