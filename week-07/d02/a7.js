'use strict'; 

var words = ["What", "I", "do", "create,", "I", "cannot", "not", "understand."];

words[5] = [words[2], words[2] = words[5]][0];

console.log(words.join(' '))
