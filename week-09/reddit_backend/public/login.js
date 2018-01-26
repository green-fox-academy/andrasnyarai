'use strict'

var nbspFix = document.querySelector('.login');
nbspFix.innerHTML = nbspFix.innerHTML.replace(/&nbsp;/g,'');

let logo = document.querySelector('.main_login > div:first-child')
let background = document.querySelector('.main_login')
let login = document.querySelector('.login')

let createAccount = document.querySelector('.send')
createAccount.addEventListener('click', function () {
    let newAccName = document.querySelector('#login-send').value
    let newPassword = document.querySelector('#password-send').value

    let newAccObj = {
        "name": newAccName,
        "password": newPassword
    }

    if (15 > newAccName.length && newAccName.length > 0 && 15 > newPassword.length && newPassword.length > 0) {

        let httpRequest = new XMLHttpRequest();
        httpRequest.open('POST', '/newaccounts', true);
        httpRequest.setRequestHeader("Accept", "application/json");
        httpRequest.setRequestHeader("Content-Type", "application/json");
        

        httpRequest.onload = function() {
            var data = JSON.parse(httpRequest.responseText);
            if (data) {
                alert('account created')
            }
        }
        httpRequest.send(JSON.stringify(newAccObj));
    }

})

let button = document.querySelector('.button')
button.addEventListener('click', function () {
    let input = document.querySelector('input').value
    let password = document.querySelector('.login > div:first-child > input:last-of-type').value

    let newObj = {
        "name": input,
        "password": password
    }

    if (15 > input.length && input.length > 0 && 15 > password.length && password.length > 0) {

        let httpRequest = new XMLHttpRequest();
        httpRequest.open('POST', '/accounts', true);
        httpRequest.setRequestHeader("Accept", "application/json");
        httpRequest.setRequestHeader("Content-Type", "application/json");
        
        httpRequest.onload = function() {
            var data = JSON.parse(httpRequest.responseText);
            if (data) {
    
                background.classList.add('out')
                login.style['opacity'] = '0'
            
                let username = input.trim()
            
                document.querySelector('input').value = `welcome ${username}`
                document.querySelector('p').textContent = '⫶'
        
                let query = `?para1=${username}`
        
                setTimeout(function () {
                    window.location.replace(`main.html${query}`);    
                },4500)
            }
        }
        httpRequest.send(JSON.stringify(newObj));
    }

})

let send = document.querySelector('.send')
send.addEventListener('click', function () {

})

logo.addEventListener('mouseover', function(){
    background.classList.add('lightning')
});
logo.addEventListener('mouseout', function(){
    background.classList.remove('lightning')
});
document.querySelector('.account').addEventListener('click', function () {
    let login = document.querySelector('.login > div:first-child')
    let create = document.querySelector('.login > div:last-child')

    login.style['display'] = 'none'
    create.classList.add('visible')
})
document.querySelector('.back').addEventListener('click', function () {
    let login = document.querySelector('.login > div:first-child')
    let create = document.querySelector('.login > div:last-child')

    login.style['display'] = 'flex'
    create.classList.remove('visible')
})