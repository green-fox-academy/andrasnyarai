# Reuse your Animal class
# Create a Farm class
# it has list of Animals
# it has slots which defines the number of free places for animals
# breed() -> creates a new animal if there's place for it
# slaughter() -> removes the least hungry animal

from animal import Animal

class Farm(object):
    def __init__(self, slots=5):
        self.slots = slots
        self.creatures = []

    def add(self, creature):
        if len(self.creatures) < self.slots:
            self.creatures.append(creature)
        else:
            return "not enough space"

    def breed(self, name, hunger=50, thirst=50):
        if self.slots == 0:
            pass
        else:
            name = Animal(name, hunger, thirst)
            self.creatures.append(name)
    
    def slaughter(self):
        self.creatures.sort(key=lambda x: x.hunger, reverse=False)
        del(self.creatures[0])

    def __str__(self):
        result = ""
        for i in range(0, len(self.creatures)):
            result += str(i + 1) + ". " + self.creatures[i].__str__() + "\n"
        return result


pig = Animal("pig",200)
cow = Animal("cow",30)
tiger = Animal("tiger",800)
badcat = Animal("badcat",100)

lui_farm = Farm()

lui_farm.add(pig)
lui_farm.add(cow)
lui_farm.add(tiger)

lui_farm.breed("raven", 10)
lui_farm.breed("elephant", 100)

lui_farm.slaughter()
print(lui_farm.add(badcat))
print(lui_farm)
lui_farm.slaughter()
print(lui_farm)