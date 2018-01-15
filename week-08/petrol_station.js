'use strict';

// Create and object called car
//  - It should store its petrol level called petrolLevel
//  - It should store its petrol capacity called petrolCapacity
//  - It should have a refill(amount) method, that increments the petrol level,
//    than returns how much petrol it consumed from the given amount
//  - Initialize the petrol level to zero and the capacity to 50 
//
// Create an object called station
//  - It should store petrol amount called petrolStorage
//  - It should have a provide(car) method that calls the refill method of the car
//    with the stored petrol amount as a parameter, then decrement the used petrol
//  - Initialize the petrol amount to 3000

const Car = {
    petrolLevel: 0,
    petrolCapacity: 50,
    refill: function(amt) {
        if (amt >= (Car.petrolCapacity - Car.petrolLevel)) {
            let amoutOFRefilled = Car.petrolCapacity - Car.petrolLevel
            Car.petrolLevel = Car.petrolCapacity;
           return amoutOFRefilled
        } else {
            Car.petrolLevel += amt;
            return amt
        }
    }
}

const Station = {
    petrolStorage: 3000,
    provide: function(auto) {
        Station.petrolStorage -= auto.refill(Station.petrolStorage)
    }
}

console.log(Car.petrolLevel);
console.log(Station.petrolStorage);

Station.provide(Car);

console.log(Car.petrolLevel);
console.log(Station.petrolStorage);