'use strict'; 

var students = [
    {'name': 'Rezso', 'age': 9.5, 'candies': 2},
    {'name': 'Gerzson', 'age': 10, 'candies': 1},
    {'name': 'Aurel', 'age': 7, 'candies': 3},
    {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

function moreThan(list) {
    let count = 0;
    for (let person of list) {
        if (person.candies > 4) {
            console.log(person.name);
        }
    }
}

function sumOf(list) {
    let sum = 0;
    for (let person of list) {
        sum += person.candies;
        
        }
    return sum / students.length;
}

moreThan(students);
console.log(sumOf(students));