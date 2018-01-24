'use strict'

let test = require('tape')
let counter = require('./count_letters.js')

let c = new counter

test('/ init try', function (t) {
  t.deepEqual(c.countLetters('hello'), {h:1, e:1, l:2, o:1})
  t.end()
})
test('/ with space', function (t) {
  t.deepEqual(c.countLetters('hel lo'), {h:1, e:1, l:2, o:1, ' ':1})
  t.end()
})
test('/ with num', function (t) {
  t.deepEqual(c.countLetters('hel lo1'), {h:1, e:1, l:2, o:1, ' ':1, '1':1})
  t.end()
})