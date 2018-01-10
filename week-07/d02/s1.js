'use strict'; 

var example = "In a dishwasher far far away";

example = example.split(' ')
example.map(function(item, index) {
    if (item == 'dishwasher') {
        example[index] = 'galaxy';
    }
})

example = example.join(' ')
console.log(example)
