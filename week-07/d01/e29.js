'use strict'; 

var lineCount = 10;

for (let a = 0; a <= lineCount; a++ ) {
    if (a == 0) {
        console.log(' ');
    } else {
        console.log(' '.repeat(lineCount - a) + '¤'.repeat(a) + '¤'.repeat(a - 1));
    }
}