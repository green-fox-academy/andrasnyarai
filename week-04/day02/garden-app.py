class Garden(object):

    def __init__(self):
        self.field = []

    def add(self,organism):
        self.field.append(organism)

    def __str__(self):
        result = ""
        for i in range(0, len(self.field)):
            result += self.field[i].__str__() + "\n"
        return result

    def watering(self,water_number):
        virtual = 0
        for i in range(len(self.field)):
            if self.field[i].water_amount <= self.field[i].water_need:
                virtual += 1
            else:
                pass
        for i in range(len(self.field)):
            if self.field[i].water_amount <= self.field[i].water_need:
                self.field[i].water_amount += (water_number/virtual)*self.field[i].water_absorb
            else:
                pass
        return print("Watering with " + str(water_number))


class Tree(object):

    def __init__(self, color, water_amount, water_absorb=0.4, water_need=10):
        self.color = color
        self.water_amount = water_amount
        self.water_absorb = water_absorb
        self.water_need = water_need

    def __str__(self):
        if self.water_amount < 10:
            return "The " + str(self.color) + " Tree needs water."
        else:
            return "The " + str(self.color) + " Tree doesnt need water."

class Flower(object):

    def __init__(self, color, water_amount, water_absorb=0.75, water_need=5):
        self.color = color
        self.water_amount = water_amount
        self.water_absorb = water_absorb
        self.water_need = water_need

    def __str__(self):
        if self.water_amount < 5:
            return "The " + str(self.color) + " Flower needs water."
        else:
            return "The " + str(self.color) + " Flower doesnt need water."

zen_garden = Garden()
t1 = Tree("Red", 8)
t2 = Tree("Green", 7)
p1 = Flower("Pink", 4)
p2 = Flower("White", 4)


zen_garden.add(t1)
zen_garden.add(t2)
zen_garden.add(p1)
zen_garden.add(p2)
print(zen_garden)
zen_garden.watering(10)
print(zen_garden)
zen_garden.watering(20)
print(zen_garden)
