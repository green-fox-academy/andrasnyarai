'use strict'; 

var args = process.argv.splice(2);

args = args.join(' ');
args = args.split('');
args = args.filter(entry => entry.trim() != '');

let operator
let splitPoint
let operators = ['+','-','/','*','%']
for (let index in args) {
    if (operators.includes(args[index])) {
        operator = args[index]
        splitPoint = index
    }
}

if (operator == '*') {
    let countA = 0;
    for (let _look_ of args) {
        if (_look_ == '*') {
            countA += 1;
        }
    } if (countA == 2) {
        operator = '**';
    }
}

let part_a = args.slice(0, splitPoint)
let part_b = args.slice(splitPoint, args.length)

function isNumeric(value) {
    return (value == Number(value)) ? true : false;
}

part_a = part_a.filter(entry => isNumeric(entry) == true )
part_b = part_b.filter(entry => isNumeric(entry) == true )
part_a = part_a.join('')
part_b = part_b.join('')

if (operator == '-' && args[1] == '-' && part_b.length > 0) {
    operator = '--'
    console.log(--part_b)
} else if (operator == '+' && args[1] == '+' && part_b.length > 0) {
    operator = '++'
    console.log(++part_b)
} else if (part_b.length > 0 && typeof operator != 'undefined' && part_a.length > 0) {
    console.log(part_a + ' ' + operator + ' ' + part_b + ' ' + '= ' + eval(part_a + operator + part_b))
}  else if (typeof operator == 'undefined') {
    console.log('no operator')
}  else if (part_b.length == 0 || part_a.length == 0) {
    console.log('nothing to do math with')
}