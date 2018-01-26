'use strict'

function validify () {

    let submitArea = document.querySelector('#submit').value.trim()
    let textAreaContent = document.querySelector('#textarea').value.trim()
    
    if (submitArea.length > 0 && textAreaContent.length > 0) {
        makePost(submitArea, textAreaContent)
    } else {
        alert('You provided no subjects!')
    }
}

function makePost(title, url) {
    
    let httpRequest = new XMLHttpRequest();
    httpRequest.open('POST', '/posts', true);
    
    httpRequest.setRequestHeader("Accept", "application/json");
    httpRequest.setRequestHeader("Content-Type", "application/json");
    httpRequest.setRequestHeader("Username", userName);

    let params = {
        "title": title,
        "url": url,
    }
    
    httpRequest.onreadystatechange = console.log
    httpRequest.onreadystatechange = function() {

        if(httpRequest.readyState == 4 && httpRequest.status == 200) {
            window.location.replace(`main.html?para1=${userName}`);
        }
    }
    httpRequest.send(JSON.stringify(params));
}

var nbspFix = document.querySelector('.form');
nbspFix.innerHTML = nbspFix.innerHTML.replace(/&nbsp;/g,'');

let button = document.querySelector('.button')
button.addEventListener('click', validify)

let userName = window.location.href.split('para1=')
userName = decodeURIComponent(userName[1])
