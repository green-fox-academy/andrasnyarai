'use strict'

let thisInput = document.querySelector('input')
let thisButton = document.querySelector('button')
let thisDiv = document.querySelector('div')

function call () {

    var sentence = thisInput.value.replace(/ /g, '+')
    var url = "https://yoda.p.mashape.com/yoda?sentence=" + sentence;
    
    $.ajax({
      url: url,
      method: 'GET',
      headers: {
        "X-Mashape-Key": "kD0uEpXfdLmshbBtzPxApb2C0lWAp1SYQo9jsn5BqjtXfvh4bu",
        "Accept": "text/plain"
      }
    }).done(function(result) {
    
    thisDiv.textContent = result
    
    }).fail(function(err) {
        throw err;
      });

}

thisButton.addEventListener('click', call)