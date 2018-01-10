'use strict'; 

let a = 12.001;
let b = 0.2;
let c = 5.5;

let Surface = 2 * ((a * b) + (b * c) + (c * a));
let Volume = a * b * c;

console.log(Surface);
console.log(Volume);