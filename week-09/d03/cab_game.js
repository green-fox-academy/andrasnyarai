'use strict'

class CAB {
    constructor (){
        this.secretNumber = this.generateRandom()
        this.counter = 0
        this.playing = true
    }
    generateRandom () {
        let number = '';
        number += Math.floor(Math.random() * (9 - 0 + 1)) + 0;
        number += Math.floor(Math.random() * (9 - 0 + 1)) + 0;
        number += Math.floor(Math.random() * (9 - 0 + 1)) + 0;
        number += Math.floor(Math.random() * (9 - 0 + 1)) + 0;
        return number
    }
    gameState (guess) {

        this.counter += 1
        this.response = ''
        this.secretNumber.split('')
        guess.split('').map((item, index) => {
            if (this.secretNumber[index] == item) {
                this.response += 'C'
            } else if (this.secretNumber.includes(item)) {
                this.response += 'B'
            } else {
                this.response += '_'
            }
        })
        return this.response
    }
    validateGuess (guess) {
        guess = '' + guess
        if (this.isNumber(guess)) {
            if (guess.length == 4) {
                return true
            } else {
                return false
            }
        }
    }
    isNumber(guess) {
        if (guess.split('').every(function (item) {
            return Number(item)
        })) {
            return true
        } else {
            return false
        }
        
    }
    flow (guess) {
        let checkIfWin = this.gameState(guess)
        if (checkIfWin == 'CCCC') {
            return `you won in - ${this.counter}`
            this.playing = false
        } else {
            return `quess again - ${checkIfWin}`
        }
    }
}

// let cabGame = new CAB()

// document.querySelector('button').addEventListener('click', function () {
//     let value = document.querySelector('input').value
//     if (cabGame.validateGuess(value)) {
//         document.querySelector('p').textContent = cabGame.flow(value)

//     }
// })

module.exports = CAB

