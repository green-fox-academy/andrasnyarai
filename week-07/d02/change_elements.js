'use strict'; 

let s = [1, 2, 3, 8, 5, 6]

s.map(function(item, index){
    if (index == 3) {
        s[index] = 4;
    };
})

console.log(s[3])
console.log(s)