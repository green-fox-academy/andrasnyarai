'use strict'; 

function factorio (input) {
    let fact = 1;
    for (let num = 1; num <= input; num++) {
        fact *= num;
    }
    return fact;
}

console.log(factorio(5))