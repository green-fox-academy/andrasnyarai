from pirates import Pirate, Captain, Ship

class Armada(object):

    def __init__(self, flag):
        self.flag = flag
        self.army_of_ships = []
        self.win = []
        self.lose = []
    
    def recruit_ships(self, ship):
        self.army_of_ships.append(ship)

    def war(self,other_armada):
        for i in range(len(self.army_of_ships) + len(other_armada.army_of_ships)):
            if len(self.army_of_ships) == 0:
                return "Win"
            if len(other_armada.army_of_ships) == 0:
                return "Lose"
            war =  self.army_of_ships[0].battle(other_armada.army_of_ships[0])
            if war == True:
                self.win.append(self.army_of_ships[0])
                other_armada.lose.append(other_armada.army_of_ships[0])
                del(other_armada.army_of_ships[0])
                i = 0
            if war == False:
                self.lose.append(self.army_of_ships[0])
                other_armada.win.append(other_armada.army_of_ships[0])
                del(self.army_of_ships[0])
                i = 0

    def __str__(self):
        result = ""
        for i in range(len(self.army_of_ships)):
            result += self.army_of_ships[i].__str__() + "\n"
        return result

jack = Captain("Jack")
jack.drink_some_rum()
ghost_renoir = Ship("ghost renoir")
ghost_renoir.fill_ship(jack)
ghost_renoir.mutiny('Coronado')

hubble = Captain("Hubble")
hubble.drink_some_rum()
white_denim = Ship("white denim")
white_denim.fill_ship(hubble)

royal_bermuda = Armada("purple stripes on white")
royal_bermuda.recruit_ships(ghost_renoir)
royal_bermuda.recruit_ships(white_denim)


mnec = Captain("Mnec")
mnec.drink_some_rum()
the_flamingo = Ship("the flamingo")
the_flamingo.fill_ship(mnec)

blazing_howl = Ship("blazing_howl")
blazing_howl.fill_ship(jack)

snake_eyes = Armada("green circle on black")
snake_eyes.recruit_ships(the_flamingo)
snake_eyes.recruit_ships(blazing_howl)

print('csata:')
print(royal_bermuda.war(snake_eyes))
print('royal lose')
print(royal_bermuda.lose)
print('royal win')
print(royal_bermuda.win)
print('snake lose')
print(snake_eyes.lose)
print('snake win')
print(snake_eyes.win)
print('royal army')
print(royal_bermuda.army_of_ships)
print('snake army')
print(snake_eyes.army_of_ships)
print('len royal army')
print(len(royal_bermuda.army_of_ships))
print('len snake army')
print(len(snake_eyes.army_of_ships))
