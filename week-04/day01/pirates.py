import random

class Pirate(object):

    def __init__(self):
        self.toxic = 0
        self.sleep = 'awake'
        self.dead = 'alive'
        self.have_parrot = 'no bird'
    
    def drink_some_rum(self,rum=random.randint(0,5)):
        if self.sleep == 'awake' and self.dead == 'alive':
            self.toxic += rum
            return "<glupp>"
        if self.dead == 'dead':
            return "he's dead"

    def hows_it_going_mate(self):
        if self.toxic <= 4 and self.sleep == 'awake' and self.dead == 'alive':
            return "Pour me anudder!"
        if self.toxic > 4 and self.sleep == 'awake' and self.dead == 'alive':
            self.sleep = 'passed out'
            return "Arghh, I'ma Pirate. How d'ya d'ink its goin?"
        if self.sleep == 'passed out':
            return "iiiiii"
        if self.dead == 'dead':
            return "I'm dead mate"

    def die(self):
        self.sleep = ''
        self.dead = 'dead'

    def brawl(self, another_pirate):
        if self.dead == 'alive' and self.sleep == 'awake' and another_pirate.dead == 'alive' and another_pirate.sleep == 'awake':
            x = random.randint(0,2)
            if x == 0:
                self.sleep = ''
                self.dead = 'dead'
                return "No rest for the wicked"
            if x == 1:
                another_pirate.sleep = ''
                another_pirate.dead = 'dead'
                return "Nice fight bro"
            if x == 2:
                self.sleep = 'passed out'
                another_pirate.sleep = 'passed out'
                return "Touché"
        else:
            return "Not today"

    def parrot(self):
        self.have_parrot = 'birdybird'

    def __str__(self):
        return "  rum consumed: " + str(self.toxic) + " status: " + self.dead + " - " + self.sleep

class Captain(Pirate):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.have_parrot = True

    def __str__(self):
        return "\nCaptain " + self.name + ", rum consumed: " + str(self.toxic) + " status: " + self.dead + " - " + self.sleep

class Ship(object):

    def __init__(self, name):
        self.name = name
        self.crew = []
        self.cabin_office = []

    def fill_ship(self, captain_name):
        y = random.randint(10,15)
        for i in range(y):
            new_2pirate = Pirate()
            new_pirate = Pirate()
            new_pirate.drink_some_rum(random.randint(0,5))
            new_2pirate.drink_some_rum(random.randint(0,5))
            new_pirate.hows_it_going_mate()
            new_2pirate.hows_it_going_mate()
            new_pirate.brawl(new_2pirate)
            self.crew.append(new_pirate)
            self.crew.append(new_2pirate)
        self.cabin_office.append(captain_name)

    def battle(self, other_ship):

        self.pirates_ready = 0
        for i in range(len(self.crew)):
            if self.crew[i].sleep == 'awake':
                self.pirates_ready += 1
            if self.crew[i].sleep == 'passed out':
                self.pirates_ready += 0.5
        for i in range(len(self.cabin_office)):
                self.pirates_ready -= self.cabin_office[i].toxic

        other_ship.pirates_ready = 0
        for i in range(len(other_ship.crew)):
            if other_ship.crew[i].sleep == 'awake':
                other_ship.pirates_ready += 1
            if other_ship.crew[i].sleep == 'passed out':
                other_ship.pirates_ready += 0.5
        for i in range(len(other_ship.cabin_office)):
                other_ship.pirates_ready -= other_ship.cabin_office[i].toxic

        if self.pirates_ready > other_ship.pirates_ready:
            z = random.randint(0,len(other_ship.crew)//2)
            other_ship.crew.sort(key=lambda x: x.dead, reverse=False)
            for i in range(z):
                if other_ship.crew[i].dead == 'alive':
                    other_ship.crew[i].dead = 'dead'
                    other_ship.crew[i].sleep = ''
            q = random.randint(0,len(self.crew)//2)
            self.crew.sort(key=lambda x: x.dead, reverse=False)
            for i in range(q):
                if self.crew[i].dead == 'alive':
                    self.crew[i].toxic += random.randint(0,5)
            self.cabin_office[0].toxic += random.randint(0,5)
            return True

        if self.pirates_ready < other_ship.pirates_ready:
            z = random.randint(0,len(self.crew)//2)
            self.crew.sort(key=lambda x: x.dead, reverse=False)
            for i in range(z):
                if self.crew[i].dead == 'alive':
                    self.crew[i].dead = 'dead'
                    self.crew[i].sleep = ''
            q = random.randint(0,len(other_ship.crew)//2)
            other_ship.crew.sort(key=lambda x: x.dead, reverse=False)
            for i in range(q):
                if other_ship.crew[i].dead == 'alive':
                    other_ship.crew[i].toxic += random.randint(0,5)
            other_ship.cabin_office[0].toxic += random.randint(0,5)
            return False

        if self.pirates_ready == other_ship.pirates_ready:
            return "the captains decided to be friends"

    def mutiny(self,leader):
        del(self.cabin_office[0])
        w = random.randint(0,len(self.crew)-1)
        self.crew[w] = Captain(leader)
        self.crew[w].drink_some_rum()
        self.cabin_office.append(self.crew[w])
        del(self.crew[w])


    def __str__(self):
        result = ""
        alive_pirates = 0
        for i in range(len(self.crew)):
            if self.crew[i].sleep == 'awake':
                alive_pirates += 1
        for i in range(len(self.cabin_office)):
            if self.cabin_office[i].sleep == 'awake':
                alive_pirates += 1
        for i in range(len(self.cabin_office)):
            result += self.cabin_office[i].__str__() + "\n"
        result += "Da crew of the " + self.name + ":\n"
        for i in range(len(self.crew)):
            result += self.crew[i].__str__() + "\n"
        result += str(alive_pirates) + " pirate(s) is capable of walking"
        return result
