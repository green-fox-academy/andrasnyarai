'use strict'; 

var todoText = " - Buy milk\n";

todoText = todoText.split('')
todoText.push(' - Download games\n\t- Diablo')
todoText = todoText.join('')

console.log(todoText);