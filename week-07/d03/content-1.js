'use strict';

alert(document.querySelector('h1').textContent);
console.log(document.querySelector('p').textContent);
alert(document.querySelector('.other').textContent);

document.querySelector('h1').textContent = 'New Content';

let change = document.querySelector('p').textContent;
document.querySelector('p.result').textContent = change;