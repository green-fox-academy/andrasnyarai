'use strict'; 

let matrix = [];

function filler (length) {
    length--
    for (let num = 0; num <= length; num++) {
        matrix.push(['▓'.repeat(length - num) + ' ◊ ' + '▓'.repeat(num)])
    }
}
filler(10)

for (let item of matrix) {
    console.log(item.join(''));
}
