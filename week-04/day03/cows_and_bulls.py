# Create a class what is capable of playing exactly one game of Cows and Bulls (CAB).
# The player have to guess a 4 digit number. For every digit that the player guessed
#  correctly in the correct place, they have a “cow”. For every digit the player guessed 
#  correctly in the wrong place is a “bull.”

# The CAB object should have a random 4 digit number, which is the goal to guess.
# The CAB object should have a state where the game state is stored (playing, finished).
# The CAB object should have a counter where it counts the guesses.
# The CAB object should have a guess method, which returns a string of the guess result
# All methods, including constructor should be tested
from random import *

class MainGame(object):

    def __init__(self):
        self.secret = self.generate()
        self.counter = 0
        self.playing = True

    def generate(self): 
        return str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9))

    def validate(self):
        self.guess_state = True
        while self.guess_state:
            self.guess = input("make a guess: ")
            if self.guess.isnumeric() and len(self.guess) == 4:
                self.counter += 1
                self.guess_state = False
            else:
                print('wrong format!')
        return self.guess
    
    def start(self):
        print('i have a random 4 digit number and you can guess it')
        while self.playing:
            x = self.secret
            y = self.validate()
            if y == x:
                print('you won, yai')
                self.playing = False
            else:
                self.cab_counter()
                print('this was your ' + str(self.counter) + '. guess, try again you have - ' + str(self.cab_state))

    def cab_counter(self):
        self.cab_state = {'C' : 0, 'B' : 0}
        for i in range(len(str(self.guess))):
            if self.guess[i] == self.secret[i]:
                self.cab_state['C'] += 1
            elif self.guess[i] in self.secret:
                self.cab_state['B'] += 1

obj = MainGame()
obj.start()
