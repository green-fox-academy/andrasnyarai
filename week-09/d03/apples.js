'use strict'

let test = require('tape')

let fruit = {
	getApple: () => 'apple'
}

test('define fruit', function (t) {

	t.equal(fruit.getApple(), 'apple')
	t.end()
})
