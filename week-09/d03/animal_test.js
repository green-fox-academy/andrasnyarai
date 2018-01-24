'use strict'

let testObject = require('C:\\Users\\Andras\\greenfox\\andrasnyarai\\week-08\\d01\\animal_farm.js')
let test = require('tape')

test('/ init object values', (t) => {
    let o = new testObject()
    t.equal(o.hunger, 5)
    t.end()
})

test('/ init function eat', (t) => {
    let o = new testObject()
    o.eat()
    t.equal(o.hunger, 4)
    t.end()
})

test('/ init function drink', (t) => {
    let o = new testObject()
    o.drink()
    t.equal(o.thirst, 4)
    t.end()
})

test('/ init play', (t) => {
    let o = new testObject()
    o.play()
    t.equal(o.thirst, 6)
    t.equal(o.hunger, 6)
    t.end()
})
