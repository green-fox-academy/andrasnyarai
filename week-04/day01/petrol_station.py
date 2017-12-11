# Create Station and Car classes
# Station
# gas_amount
# refill(car) -> decreases the gasAmount by the capacity of the car and increases the cars gas_amount
# Car
# gas_amount
# capacity
# create constructor for Car where:
# initialize gas_amount -> 0
# initialize capacity -> 100

class Station(object):

    def __init__(self,gas_amount=1000):
        self.gas_amount = gas_amount

    def refill(self,car):
        car.gas_amount += car.capacity
        self.gas_amount -= car.capacity

    def check_station(self):
        return self.gas_amount

class Car(object):

    def __init__(self,gas_amount=0,capacity=100):
        self.gas_amount = gas_amount
        self.capacity = capacity

    def check_car(self):
        return self.gas_amount

oil = Station()
bmw = Car()

print('initial gas station oil count: ', oil.check_station())
print('initial car oil count: ', bmw.check_car())

oil.refill(bmw)

print('gas station after refill: ', oil.check_station())
print('car after refill: ', bmw.check_car())


