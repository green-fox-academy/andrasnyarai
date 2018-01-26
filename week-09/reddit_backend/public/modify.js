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
    httpRequest.open('PATCH', 'posts/'+id, true);
    
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
newId.splice(0,2)
newId.splice(newId.length - 1, 1)
newId = newId.join('')
id = newId

let userName = decodeURIComponent(fillData[4]).split('')
userName.splice(0,2)
userName = userName.join('')

document.querySelector('.form > #submit').value = newTitle
document.querySelector('.form > #textarea').value = newUrl