'use strict'

let fib = require('./fibonacci.js')
let test = require('tape')

test('/ init test', (t) => {
    t.equal(fib(10), 55)
    t.end()
})
test('/ with zero', (t) => {
    t.equal(fib(0), 0)
    t.end()
})
test('/ with negative', (t) => {
    t.equal(fib(-1), 0)
    t.end()
})