'use strict'; 

function sum (parameter) {
    let sum = 0
    for (let num = 0; num <= parameter; num++) {
        sum += num;
    }
    return sum;
}

console.log(sum(4));