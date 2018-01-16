'use strict';

// Implement the selectLastEvenNumber function that takes an array and callback,
// it should call the callback immediately with the last even number on the array

function printNumber(num) {
  console.log(num);
}

function selectLastEvenNumber (array, subFunction) {
    let newArray = array.reverse()
    let mark;
    let found = false
    for (let i in newArray) {
        if (newArray[i] % 2 == 0) {
            mark = i
            let found = true
            if (found) {
                for (let i in array) {
                    if (i == mark) {
                        subFunction(array[i])
                        return
                    }
                }
            }
        }
    }
}

selectLastEvenNumber([2, 5, 7, 8, 9, 11], printNumber); // should print 8