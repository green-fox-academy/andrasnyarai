# Create Animal class
# Every animal has a hunger value, which is a whole number
# Every animal has a thirst value, which is a whole number
# when creating a new animal object these values are created with the default 50 value
# Every animal can eat() which decreases their hunger by one
# Every animal can drink() which decreases their thirst by one
# Every animal can play() which increases both by one

class Animal(object):

    def __init__(self,name, hunger=50, thirst=50):
        self.name = name
        self.hunger = hunger
        self.thirst = thirst

    def eat(self):
        self.hunger -= 1
        return self.hunger

    def drink(self):
        self.thirst -= 1
        return self.thirst

    def play(self):
        self.hunger += 1
        self.thirst += 1
        return self.hunger, self.thirst

    def __str__(self):
        return self.name

    


lion = Animal('lion')

print(lion.hunger)

lion.eat()

print(lion.hunger)

lion.drink()

print(lion.thirst)

lion.play()

print(lion.hunger, lion.thirst)

print(lion)
