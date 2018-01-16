'use strict'

// Gather 10.000 candies!
// Clicking the ‘Create candies’ button gives you 1 candy.
// You can buy a lollipop for 100 candies by clicking the ‘Buy lollipop’ button.
// 10 lollipops generate 1 candy per second.
// Use the 🍭 emoji to display the lollipops you have
// Display the candy producton rate in the Candies / Second row
// If you press the "make candy rain" button, the candy generation should speed up 10x

let createC = document.querySelector('.create-candies')
let buyL = document.querySelector('.buy-lollypops')
let rain = document.querySelector('.candy-machine')

let candyStore = document.querySelector('.candies')
let lollyStore = document.querySelector('.lollypops')
let rainStore = document.querySelector('.speed')

let candyCounter = 0
let lollyCounter = 3
let generateSec = 1


createC.addEventListener('click', function() {
    candyCounter += 100
    candyStore.textContent = candyCounter;
})

buyL.addEventListener('click', function() {
    if (candyCounter >= 100) {
        candyCounter -= 100;
        candyStore.textContent = candyCounter;
        lollyCounter += 1;
        lollyStore.innerHTML += '🍭'
    }
})

function speedOfCandies () {
    let speed = 1000
    return {
        speed: 1000,
        productionRate: function loop() {
            setTimeout(function () {
                let bonus = Math.floor(lollyCounter/10)
                if (lollyCounter >= 10) {
                    candyCounter += bonus
                    candyStore.textContent = candyCounter;
                    rainStore.textContent = bonus;
                }
                loop();
            }, speed);
        },
        speedUp: function() {
            if (speed > 1) {
                speed /= 10
            }
        }
    }
}

let speedUnit = speedOfCandies()
speedUnit.productionRate()

rain.addEventListener('click',speedUnit.speedUp)
