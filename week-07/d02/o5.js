'use strict'; 

const ingredients = [
	{ "name": "vodka", "in_stock": 1, "needs_cooling": true },
	{ "name": "coffee_liqueur", "in_stock": 0, "needs_cooling": true },
	{ "name": "fresh_cream", "in_stock": 1, "needs_cooling": true },
	{ "name": "captain_morgan_rum", "in_stock": 2, "needs_cooling": true },
	{ "name": "mint_leaves", "in_stock": 0, "needs_cooling": false },
	{ "name": "sugar", "in_stock": 0, "needs_cooling": false },
	{ "name": "lime juice", "in_stock": 0, "needs_cooling": true },
	{ "name": "soda", "in_stock": 0, "needs_cooling": true }
]

let maxLength = 0;
for (let item of ingredients) {
    if (item.name.length > maxLength) {
        maxLength = item.name.length
    }
}
console.log(maxLength)

for (let item of ingredients) {
    if (item.in_stock == 0) {
        item.in_stock = '─';
    } 
}
for (let item of ingredients) {
    if (item.needs_cooling == true) {
        item.needs_cooling = 'Yes';
    } else if (item.needs_cooling == false) {
        item.needs_cooling = 'No ';
    }
}
let titleOne = 'Ingredient'
let titleTwo = 'Needs cooling'
let titleThree = 'In stock'

console.log('┌─' + '─'.repeat(maxLength) + '─┬─' + '─'.repeat(titleTwo.length) + '─┬─' + '─'.repeat(titleThree.length) + '─┐')

console.log('│' + titleOne + ' '.repeat(maxLength - titleOne.length + 2) + '│' + titleTwo + ' '.repeat(titleTwo.length - 11) + '│' + titleThree + ' '.repeat(titleThree.length - 7) + ' │')

console.log('├─' + '─'.repeat(maxLength) + '─┼─' + '─'.repeat(titleTwo.length) + '─┼─' + '─'.repeat(titleThree.length) + '─┤')

for (let item of ingredients) {
    console.log('│' + item.name + ' '.repeat(maxLength - item.name.length + 2) + '│' + item.needs_cooling + ' '.repeat(titleTwo.length - 1) + '│' + item.in_stock + ' '.repeat(titleThree.length) + ' │')
}
console.log('└─' + '─'.repeat(maxLength) + '─┴─' + '─'.repeat(titleTwo.length) + '─┴─' + '─'.repeat(titleThree.length) + '─┘')