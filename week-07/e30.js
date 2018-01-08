'use strict'; 

var lineCount = 9;


for (let a = 0; a <= lineCount; a++ ) {
    if (lineCount % 2 == 0) {
        var c = 0;
    } else if (lineCount % 2 >= 0) {
        var c = 1;
    }
    let b = lineCount / 2 + 1;
    if (a == 0) {
        console.log(' ');
    } else if (a <= lineCount / 2) {
        console.log(' '.repeat(lineCount - a - lineCount / 2 + c) + '¤'.repeat(a) + '¤'.repeat(a - 1));
    } else {
        b -=a - lineCount / 2;
        if (b > 0) {
            console.log(' '.repeat(lineCount - b - lineCount / 2 + c) + '¤'.repeat(b) + '¤'.repeat(b - 1));
        } 
    }
}