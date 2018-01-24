'use strict';

// Adds a and b, returns as result
const addNumbers = function(a, b) {
    if (typeof a == 'string' || typeof b == 'string') {
        throw Error('Invalid value')
    } else {
        return a + b;
    }
}

// Returns the highest value from the three given params
const maxOfThree = function(a, b, c) {
    if (typeof a == 'string' || typeof b == 'string' || typeof c == 'string') {
        throw Error('Invalid value')
    } else {
        let newList = [a, b, c].sort((a, b) => b - a)
        return newList[0]
    }
}

//Returns the median value of a list given as param
const median = function(pool){
    let counter = 0
    pool.forEach((item) => {
        if (typeof item != 'number') counter++;
    })
    if (counter > 0) {
        throw Error('Invalid value')
    } else {
        pool = pool.sort((a, b) => a - b)
        if (pool.length % 2 == 0) {
            return (pool[pool.length / 2 - 1] + pool[pool.length / 2]) / 2;
        } else if (pool.length % 2 > 0) {
            return(pool[(pool.length - 1) / 2]);
        }
    }
}

// Returns true if the param is a vovel
const isVovel = function(char){
    if (char == '' || char.length > 1) {
      throw Error('Please, give me one character')
    } else {
      return 'aeiouéáőűöüóí'.indexOf(char) > -1;

    }
}

// Create a method that translates hungarian into the teve language
const translate = function(hungarian) {
    if (typeof hungarian != 'string') {
        throw Error('Invalid value')
    } else {
        let text = hungarian.split('');
        let teve = '';
        text.forEach(function(char){
          if (isVovel(char)){
            teve += char + 'v'+ char;
          } else {
              teve += char
          }
        });
        return teve;
    }
}

module.exports = {
  addNumbers: addNumbers,
  maxOfThree: maxOfThree,
  median: median,
  isVovel: isVovel,
  translate: translate
}