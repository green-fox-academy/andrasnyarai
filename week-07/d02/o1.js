'use strict'; 

var students = [
        {'name': 'Teodor', 'age': 3, 'candies': 2},
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
]

function overallCandies(list) {
    let count = 0;
    for (let person of list) {
        count += person.candies;
    }
    return count;
}

function ageSum(list) {
    let overallAge = 0;
    for (let person of list) {
        if (person.candies < 5) {
            overallAge += person.age;
        }
    }
    return overallAge;
}

console.log(overallCandies(students))
console.log(ageSum(students))