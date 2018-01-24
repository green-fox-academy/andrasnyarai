'use strict'

let test = require('tape')

class summing {
  sum(arr) {
    arr = arr.filter((item) => typeof item === 'number')
    return arr.reduce((a, b) => a + b, 0)
    }
}

let math = new summing()

test('/ sum is equal or not', (t) => {
  let listOfInt = [1, 2, 3]
  t.equal(math.sum(listOfInt), 6)    
  t.end()
})
test('/ with one lement', (t) => {
  let listOfInt = [1]
  t.equal(math.sum(listOfInt), 1)    
  t.end()
})
test('/ sum is with empty', (t) => {
  let listOfInt = []
  t.equal(math.sum(listOfInt), 0)    
  t.end()
})
test('/ sum is with null in it', (t) => {
  let listOfInt = [null, 1]
  t.equal(math.sum(listOfInt), 1)    
  t.end()
})
test('/ strings should be ignored', (t) => {
  let listOfInt = ['string', 1, 'another', 2]
  t.equal(math.sum(listOfInt), 3)    
  t.end()
})

