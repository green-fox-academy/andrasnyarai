'use strict'

const Panama = {
    cash: 0,
    name: 'Panama',
    tax: '1%',
    deposit: function(amt) {
        Cyprus.cash += amt
        Panama.cash -= amt
    }
}

const Cyprus = {
    cash: 0,
    name: 'Cyprus',
    tax: '5%',
    deposit: function(amt) {
        Panama.cash += amt
        Cyprus.cash -= amt
    }
}

const Shuffler = {
    cash: 10000,
    pick: function()  {
        let pickCount = Math.round(Math.random())
        if (pickCount == 0) {
            Shuffler.cash -= 1000;
            Panama.cash += 1000;
            console.log('Panama got 1000')
        } else if (pickCount == 1) {
            Shuffler.cash -= 1000;
            Cyprus.cash += 1000;
            console.log('Cyprus got 1000')
        }
    }
}

Shuffler.pick() // prints Panama got 1000
Shuffler.pick() // prints Cyprus got 1000
Shuffler.pick() // prints Panama got 1000
Shuffler.pick() // prints Cyprus got 1000

Cyprus.deposit(1.1)
Panama.deposit(9.999)

console.log( Panama.cash ) // 2000 
console.log( Cyprus.cash ) // 2000 
console.log( Shuffler.cash ) // 2000 