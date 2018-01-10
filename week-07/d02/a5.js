'use strict'; 

var numbers = [1,2,3,4,5,7,8];

function _if_ (list) {
    let status = false;
    for (let num of list) {
        if (num == 7) {
            status = true;
        }
    }
    if (status == true) {
        console.log('Huuuuray');
    } else {
        console.log('noooooo')
    }
}

_if_(numbers)