// Search back in your own project the Sharpie class you made on the OO workshop
// Create tests that covers all types of input (like in the previous workshop exercise)

'use strict'

let testObject = require('C:\\Users\\Andras\\greenfox\\andrasnyarai\\week-08\\d01\\sharpie')
let test = require('tape')


test('/ init object values', (t) => {
    let o = new testObject('pink', 50)
    t.equal(o.color, 'pink')
    t.end()
})

test('/ function use', (t) => {
    let o = new testObject('pink', 25)
    o.use()
    t.equal(o.inkAmount, 75)
    t.end()
})

test('/ function use until zero', (t) => {
    let o = new testObject('pink', 75)
    o.use()
    o.use()
    t.equal(o.inkAmount, 0)
    t.end()
})

test('/ function useAll', (t) => {
    let o = new testObject('pink', 10)
    o.useAll()
    t.equal(o.inkAmount, 0)
    t.end()
})

