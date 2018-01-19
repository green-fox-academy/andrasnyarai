'use strict'

function validify () {

    let submitArea = document.querySelector('#submit').value.trim()
    let textAreaContent = document.querySelector('#textarea').value.trim()
    
    if (submitArea.length > 0 && textAreaContent.length > 0) {
        console.log(submitArea, textAreaContent)
        makePost(submitArea, textAreaContent)
    } else {
        alert('You provided no subjects!')
    }
}

function makePost(title, url) {
    
    let httpRequest = new XMLHttpRequest();
    // httpRequest.open('POST', 'http://secure-reddit.herokuapp.com/simple/posts', true);
    httpRequest.open('POST', 'https://time-radish.glitch.me/posts', true);
    
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

function deletePost () {
    let httpRequest = new XMLHttpRequest();
    httpRequest.open('DELETE', 'https://time-radish.glitch.me/posts/' + id, true);
    
    httpRequest.setRequestHeader("Accept", "application/json");
    httpRequest.setRequestHeader("Content-Type", "application/json");
    
    httpRequest.onreadystatechange = console.log

    httpRequest.onreadystatechange = function() {
        console.log(httpRequest.readyState)
    
        console.log(httpRequest.status)
    
        console.log(httpRequest.responseText)
        
        if(httpRequest.readyState == 4 && httpRequest.status == 200) {
        }
    }
    httpRequest.send(null);
    alert(httpRequest.responseText);
}


// console.log(JSON.stringify(params))


var nbspFix = document.querySelector('.form');
nbspFix.innerHTML = nbspFix.innerHTML.replace(/&nbsp;/g,'');

let button = document.querySelector('.button')
button.addEventListener('click', validify)

// Upvote()

// d_E()
