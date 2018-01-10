'use strict'; 

let ind = [4,8,12,16]

var listOfNumbers = [2, 4, 6, 8, 10, 12, 14, 16]

function numChecker (list) {
    let counter = 0;
    for (let num of list) {
        for (let i of ind) {
            if (num == i) {
                counter += 1;
            }
        }
    };
    if (counter == 4) {
        return true;
    } else {
        return false;
    }
}

console.log(numChecker(listOfNumbers));