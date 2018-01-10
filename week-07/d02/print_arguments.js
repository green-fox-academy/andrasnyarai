'use strict'; 

function printer () {
    let args = [...arguments];
    console.log(args);
}

printer('asd', 1, true);