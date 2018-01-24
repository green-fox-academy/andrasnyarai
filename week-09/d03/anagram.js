'use strict'

let test = require('tape')

let anagramValidify= (strOne, strTwo) => {
    strOne = strOne.toLowerCase().replace(' ','').split('').sort().join('')
    strTwo = strTwo.toLowerCase().replace(' ','').split('').sort().join('')
    return strOne === strTwo
}

test('/if works with words', (t) => {
    t.equal(anagramValidify('listen','silent'), true)
    t.end()
})
test('/if works with capital', (t) => {
    t.equal(anagramValidify('Listen','Silent'), true)
    t.end()
})
test('/if works with spaces', (t) => {
    t.equal(anagramValidify('list en','silent'), true)
    t.end()
})
