'use strict'; 

var currentHours = 14;
var currentMinutes = 34;
var currentSeconds = 42;

let FullTime = 24 * 60 * 60;
console.log(FullTime - (currentHours * currentMinutes * currentSeconds) + ' -left over seconds');