from pirates import Pirate, Captain, Ship

jack = Captain("Jack")
jack.drink_some_rum()

ghost_renoir = Ship("ghost renoir")
ghost_renoir.fill_ship(jack)

hubble = Captain("Hubble")
hubble.drink_some_rum()

white_denim = Ship("white denim")
white_denim.fill_ship(hubble)

ghost_renoir.mutiny('Coronado')

print(ghost_renoir.battle(white_denim))
print(ghost_renoir)

class Armada(object):

    def __init__(self, flag):
        self.flag = flag
        self.army_of_ships = []
    
    def recruit_ships(self, ship):
        self.army_of_ships.append(ship)

    def war(self,other_armada):
        for i in range(len(self.army_of_ships)):
            if self.army_of_ships[i].battle(other_armada.army_of_ships[i]):
                self.army_of_ships[i].battle(other_armada.army_of_ships[i+1])
            else:
                self.army_of_ships[i+1].battle(other_armada.army_of_ships[i])

    def __str__(self):
        result = ""
        for i in range(len(self.army_of_ships)):
            result += self.army_of_ships[i].__str__() + "\n"
        return result




mnec = Captain("Mnec")
mnec.drink_some_rum()

the_flamingo = Ship("the flamingo")
the_flamingo.fill_ship(mnec)

blazing_howl = Ship("blazing_howl")
white_denim.fill_ship(jack)

royal_bermuda = Armada("purple stripes on white")

royal_bermuda.recruit_ships(ghost_renoir)
royal_bermuda.recruit_ships(white_denim)

snake_eyes = Armada("green circle on black")

snake_eyes.recruit_ships(the_flamingo)
snake_eyes.recruit_ships(blazing_howl)

# print(royal_bermuda.war(snake_eyes))
