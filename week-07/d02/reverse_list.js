'use strict'; 

let aj = [3, 4, 5, 6, 7];

function reverser(list) {
    let temp = [];
    for (let index = list.length - 1; index >= 0; index--) {
        temp.push(list[index]);
    }
    return temp
}

console.log(aj)
console.log(reverser(aj))
console.log(aj.reverse())