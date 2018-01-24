'use strict'

let testObject = require('./cab_game.js')
let test = require('tape')

test('/ init of game object', (t) => {
	let o = new testObject()
	t.equal(9999 >= Number(o.secretNumber) >= 0, true)
	t.end()
})

test('/ validate guess', (t) => {
	let o = new testObject()
	t.equal(o.validateGuess(1111), true)
	t.end()
})

test('/ validate guess with string', (t) => {
	let o = new testObject()
	t.equal(o.isNumber('123a'), false)
	t.end()
})

test('/ check gamestate', (t) => {
	let o = new testObject()
	o.secretNumber = '1234'
	t.equal(o.gameState('1111'),'CBBB')
	t.end()
})