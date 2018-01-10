'use strict'; 

var quote = "Hofstadter's Law: It you expect, even when you take into account Hofstadter's Law."

let part1 = quote.slice(0,quote.search('It') + 2)
let part2 = quote.slice(quote.search('you'))

let insert = " always takes longer than "

quote = part1 + insert + part2

console.log(quote);

