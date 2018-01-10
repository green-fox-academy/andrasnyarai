'use strict'; 

var watchlist = []

var security_alchol_loot = 0

var queue = [
	{ 'name': 'Amanda', 'alcohol': 10, 'guns': 1 },
	{ 'name': 'Tibi', 'alcohol': 0, 'guns': 0 },
	{ 'name': 'Dolores', 'alcohol': 0, 'guns': 1 },
	{ 'name': 'Wade', 'alcohol': 1, 'guns': 1 },
	{ 'name': 'Anna', 'alcohol': 10, 'guns': 0 },
	{ 'name': 'Rob', 'alcohol': 2, 'guns': 0 },
	{ 'name': 'Joerg', 'alcohol': 20, 'guns': 0 }
]

function securityCheck () {
    let canAppend = []
    for (let person of queue) {
        if (person.guns != 0) {
            person.guns = 0;
            watchlist.push(person.name);
        }  else if (person.alcohol >= 0) {
            canAppend.push(person.name)
            security_alchol_loot += person.alcohol;
            person.alcohol = 0;
        }
    }
    queue.map(function(item, index) {
        for (let name of watchlist) {
            if (item.name == name) {
                delete queue[index]
            }
        }
    })
    queue = queue.filter(function(n){return n; });
    return canAppend;
}

console.log(securityCheck())
console.log(watchlist)
console.log(security_alchol_loot)
console.log(queue)