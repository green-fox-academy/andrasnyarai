'use strict'

class ElevatorController {
    constructor () {
        this.model = new ElevatorModel(10,5)
        this.view = new ElevatorView()
        this.events()
    }
    events() {
        var buttonUp = document.querySelector('.left > div:first-child > button:first-child')
        var buttonDown = document.querySelector('.left > div:first-child > button:last-child')
        var buttonAdd = document.querySelector('.left > div:last-child > button:first-child')
        var buttonRemove = document.querySelector('.left > div:last-child > button:last-child')

        buttonUp.addEventListener('click', this.model.upLift.bind(this.model))
        buttonDown.addEventListener('click', this.model.downLift.bind(this.model))
        buttonAdd.addEventListener('click', this.model.addPeople.bind(this.model))
        buttonRemove.addEventListener('click', this.model.removePeople.bind(this.model))
    }
}
class ElevatorModel {
    constructor (maxFloor, maxPeople) {
        this.maxFloor = maxFloor;
        this.people = maxPeople;
        this.ePos = 1;
        this.pplInE = 0;
        
        let container = document.querySelector('.e_container');
        let newDiv = document.createElement('div');
        let elevator = document.createElement('p')
        elevator.classList.add('elevator')
        elevator.innerHTML = this.pplInE;
        newDiv.style['position'] = 'relative'
        newDiv.appendChild(elevator)
        container.appendChild(newDiv)

        let floors = document.querySelector('.floors');
        let otherDiv = document.createElement('div');
        floors.appendChild(otherDiv)

        let randomnumber = Math.floor(Math.random() * (10 - 0 + 1)) + 0;
        
        otherDiv.dataset.numberOfPeople = randomnumber
        otherDiv.textContent = otherDiv.dataset.numberOfPeople
        
        
        this.elevator = document.querySelector('.elevator')
        
        for (let i = 1; i < this.maxFloor; i++) {
            let container = document.querySelector('.e_container');
            let newDiv = document.createElement('div');
            container.appendChild(newDiv)
            let floors = document.querySelector('.floors');
            let otherDiv = document.createElement('div');
            
            let randomnumber = Math.floor(Math.random() * (10 - 0 + 1)) + 0;
            otherDiv.dataset.numberOfPeople = randomnumber
            otherDiv.textContent = otherDiv.dataset.numberOfPeople

            floors.appendChild(otherDiv)
        }
    }
    upLift() {
        if (this.ePos == this.maxFloor) {
            return
        } else {
            this.ePos += 1;
            this.elevator.style['bottom'] = (this.ePos - 1) +'00%'
        }
        
    }
    downLift() {
        if (this.ePos == 1) {
            return
        } else {
           this.ePos -= 1;
           this.elevator.style['bottom'] = (this.ePos - 1) +'00%'
        }
    }
    addPeople() {
        if (this.pplInE < this.people) {

            let currentFloor = document.querySelector('.floors > div:nth-of-type(' + this.ePos + ')')
            if (currentFloor.textContent > 0) {
                
                this.pplInE += 1;
                this.elevator.textContent = this.pplInE
                currentFloor.textContent -= 1
            }
        }
    }
    removePeople() {
        if (this.elevator.textContent == '0') {
            return
        } else {
            this.pplInE -= 1;
            this.elevator.textContent = this.pplInE
            let currentFloor = document.querySelector('.floors > div:nth-of-type(' + this.ePos + ')')
            currentFloor.innerHTML = Number(currentFloor.textContent) + 1
        }
    }
}
class ElevatorView {

}

let start = new ElevatorController()