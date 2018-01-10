'use strict';

let nimals = ["kuty", "macsk", "cic"];

nimals.map(function(item, index){
    nimals[index] = item + 'a';
})

console.log(nimals);