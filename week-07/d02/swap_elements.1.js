'use strict'; 

let abc = ["Arthur", "Boe", "Chloe"];

abc[0] = [abc[2], abc[2] = abc[0]][0];

console.log(abc);