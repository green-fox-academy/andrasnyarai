'use strict';

var fruits = [
  'melon',
  'apple',
  'strawberry',
  'blueberry',
  'pear',
  'banana'
];

// Create a new array of consists numbers that shows how many times the 'e' letter
// occurs in the word stored under the same index at the fruits array!
// Please use the map method.

var HowManyE = new Array()

fruits.map(function (item, index) {
    let word = item.split('')
    let count = 0
    for (let letter of word) {
        if (letter == 'e') {
            count += 1
        }
    }
    HowManyE.push(count)
})

console.log(HowManyE)