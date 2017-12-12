class Aircraft(object):

    def __init__(self, a_type, ammo=0):
        if a_type == 'F16':
            self.a_type = a_type
            self.max_ammo = 8
            self.base_damage = 30
            self.ammo = ammo
        if a_type == 'F35':
            self.a_type = a_type
            self.max_ammo = 12
            self.base_damage = 50
            self.ammo = ammo
        else:
            self.a_type = 'F16'

    @property
    def a_type(self):
        return self.__a_type

    @a_type.setter
    def a_type(self, a_type):
        if a_type == 'F16' or a_type == 'F35':
            self.__a_type = a_type
        else:
            pass

    def fight(self):
        damage = self.base_damage * self.ammo
        self.ammo = 0
        return damage

    def refill(self, number):
        if number < self.max_ammo - self.ammo:
            self.ammo += number
            return 0
        if number > self.max_ammo - self.ammo:
            self.ammo = self.max_ammo
            return number - self.ammo

    def gettype(self):
        return str(self.a_type)

    def getstatus(self):
        return "Type "+ self.a_type + ", Ammo: " + str(self.ammo) + ", Base Damage: "+ str(self.base_damage) + ", All Damage: " + str(self.ammo*self.base_damage)

    def __str__(self):
        return "Type "+ self.a_type + ", Ammo: " + str(self.ammo) + ", Base Damage: "+ str(self.base_damage) + ", All Damage: " + str(self.ammo*self.base_damage)


# addAircraft
# It should take a string as the type of the aircraft (F16 / F35) and add a new aircraft to its store
# fill
# It should fill all the aircraft with ammo and substract the needed ammo from the ammo storage
# If there is not enough ammo than it should start to fill the F35 types first
# If there is no ammo when this method is called it should throw an exception
# fight
# It should take another carrier as a refrence parameter and fire all the ammo from the aircrafts to it, than substract all the damage from it's health points
# getStatus

class AircraftCarrier(object):

    def __init__(self,store,hp):
        self.storage = []
        self.store = store
        self.hp = hp
    
    def fill(self):
        print('filled up')
        if self.store == 0:
            return print('NO MORE')
        count = 0
        for i in range(len(self.storage)):
            count += self.storage[i].max_ammo - self.storage[i].ammo
            if self.store > count:
                for i in range(len(self.storage)):
                    self.storage[i].ammo = self.storage[i].max_ammo
                self.store -= count
            if self.store < count:
                for i in range(len(self.storage)):
                    if self.storage[i].a_type == 'F16' and self.store >= self.storage[i].max_ammo:
                        self.storage[i].ammo = self.storage[i].max_ammo
                        self.store = self.store - self.storage[i].max_ammo
                    elif self.storage[i].a_type == 'F16' and 0 < self.store < self.storage[i].max_ammo:
                        self.storage[i].ammo = self.store
                        self.store = 0
                if self.store > 0:
                    for i in range(len(self.storage)):
                        if self.storage[i].a_type == 'F35' and self.store >= self.storage[i].max_ammo:
                            self.storage[i].ammo = self.storage[i].max_ammo
                            self.store = self.store - self.storage[i].max_ammo
                        elif self.storage[i].a_type == 'F35' and 0 < self.store < self.storage[i].max_ammo:
                            self.storage[i].ammo = self.store
                            self.store = 0

    def fight(self, enemy):
        damage_counter = 0
        for i in range(len(self.storage)):
            damage_counter += self.storage[i].ammo * self.storage[i].base_damage
        for j in range(len(self.storage)):
            self.storage[j].ammo = 0
        enemy.hp -= damage_counter

    def addaircraft(self,name):
        if name == 'F16':
            new = Aircraft(name)
            self.storage.append(new)
        if name == 'F35':
            new = Aircraft(name)
            self.storage.append(new)
        else:
            pass

    def __str__(self):
        result = ""
        for i in range(0, len(self.storage)):
            result += str(i+1) + ". " + self.storage[i].__str__() + "\n"
        return result

    def getstatus(self):
        if self.hp <= 0:
            return "We are dead!"
        else:
            result = ""

            damage_counter = 0
            for i in range(len(self.storage)):
                damage_counter += self.storage[i].ammo * self.storage[i].base_damage

            result += "| HP: " + str(self.hp) + " | Aircraft count: " + str(len(self.storage)) + " | Ammo storage: " + str(self.store) + " | Total damage: "+ str(damage_counter) + "\n" + "Aircrafts:" + "\n" 
            for i in range(0, len(self.storage)):
                result += self.storage[i].__str__() + "\n"
            return result

f1 = Aircraft('F16', 5)
f2 = Aircraft('F35')
f3 = Aircraft('BBBB')

print(f3.gettype())
print(f1.fight())
print(f1.gettype())
print(f1.getstatus())
print(f1.refill(50))
print(f1.getstatus())

sun = AircraftCarrier(22,1000)

sun.addaircraft('F16')
sun.addaircraft('F16')
sun.addaircraft('F35')


print(sun)
sun.fill()
print(sun)

print(sun.getstatus())

pop = AircraftCarrier(10,500)

sun.fight(pop)

print(pop.getstatus())

print(sun.getstatus())

sun.fill()

print(sun.getstatus())