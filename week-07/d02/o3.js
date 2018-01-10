'use strict'; 

var accounts = [
	{ 'client_name': 'Igor', 'account_number': 11234543, 'balance': 203004099.2 },
	{ 'client_name': 'Vladimir', 'account_number': 43546731, 'balance': 5204100071.23 },
	{ 'client_name': 'Sergei', 'account_number': 23456311, 'balance': 1353600.0 }
]

function getAccount (index) {
    return accounts[index].client_name + ' ' + accounts[index].balance;
}

function transfer (from, to, amount) {
    let state = 0
    for (let acc of accounts) {
        if (acc.account_number == from) {
            acc.balance -= amount;
            state += 1;
        } else if (acc.account_number == to) {
            acc.balance += amount;
            state += 1;
        }
    }
    if (state < 2) {
        return '404'
    }
}

console.log(getAccount(0))
console.log(getAccount(1))
console.log(getAccount(2))
console.log(transfer(11234543, 23456311, 9999999))
console.log(getAccount(0))
console.log(getAccount(1))
console.log(getAccount(2))
console.log(transfer(1010110, 101010, 4443434))