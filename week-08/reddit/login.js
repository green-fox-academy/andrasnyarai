'use strict'

var nbspFix = document.querySelector('.form');
nbspFix.innerHTML = nbspFix.innerHTML.replace(/&nbsp;/g,'');

let logo = document.querySelector('.main_login > div:first-child')
let background = document.querySelector('.main_login')
let login = document.querySelector('.login')

let button = document.querySelector('.button')
button.addEventListener('click', function () {
    let input = document.querySelector('input').value
    if (15 > input.length && input.length > 0) {

        background.classList.add('out')
        login.style['opacity'] = '0'
    
        let username = input.trim()
    
        document.querySelector('input').value = `welcome ${username} ⪾`
        document.querySelector('p').textContent = '⫶'

        let query = `?para1=${username}`

        setTimeout(function () {
            window.location.replace(`file:///C:/Users/Andras/greenfox/andrasnyarai/week-08/reddit/index.html${query}`);    
        },4500)
    }
})

logo.addEventListener('mouseover', function(){
    background.classList.add('lightning')
});
logo.addEventListener('mouseout', function(){
    background.classList.remove('lightning')
});