'use strict'; 

let ag = ['Gin', 'Whiskey', 'Wine', 'Beer'];

ag.map(function(item, index){
    ag[index] = item.repeat(2);
})

console.log(ag);