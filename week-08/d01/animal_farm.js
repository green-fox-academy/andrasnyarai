'use strict'

class Animal {
    constructor () {
        this.hunger = 5;
        this.thirst = 5;
    }
    eat () {
        this.hunger -= 1;
    }
    drink () {
        this.thirst -= 1;
    }
    play () {
        this.hunger += 1;
        this.thirst += 1;
    }
}

module.exports = Animal


class Farm {
    constructor (freeSpaces) {
        this.spaces = freeSpaces
        this.animals = new Array(freeSpaces)
        for (let i = 0; i < freeSpaces; i++) {
            let newAnimal = new Animal();
            this.animals[i] = newAnimal;
        }
    }
    breed () {
        if (this.animals.length < this.spaces) {
            let newAnimal = new Animal();
            this.animals.push(newAnimal);
        } else {
            console.log('The stack is full')
        }
    }
    slaughter () {
        let mark = this.animals[0].hunger;
        let subject = 0;
        for (let index in this.animals) {
            if (this.animals[index].hunger < mark) {
                subject = index;
            }
        }
        this.animals.splice(subject, 1)
    }
    printState () {
        if (this.animals.length == 0) {
            var suffix = 'bankrupt'
        } else if (this.spaces > this.animals.length > 0) {
            var suffix = 'okay'
        } else if (this.animals.length == this.spaces) {
            var suffix = 'full'
        }
        console.log('we have ' + this.animals.length + ' living animals ' + 'we are ' + suffix)
    }
    progress () {
        for (let i in this.animals) {
            let maximum = 2
            let minimum = 0
            let randomnumber = Math.floor(Math.random() * (maximum - minimum + 1)) + minimum;

            if (randomnumber == 0) {
                this.animals[i].eat()
            } else if (randomnumber == 1) {
                this.animals[i].drink() 
            } else if (randomnumber == 2) {
                this.animals[i].play()
            }

        }
        this.slaughter()
        this.breed()
        this.printState()
    }
}

// const SheepFarm = new Farm(20);

// const button = document.querySelector('button');
// let progress = SheepFarm.progress.bind(SheepFarm)
// button.addEventListener('click', progress)

