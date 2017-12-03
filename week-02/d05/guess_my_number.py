import random

right_range = False
while not right_range:
    range_user = input("Give me the maximum value of the random number: ")
    right_range = range_user.isnumeric()

r = random.randint(1, int(range_user))
win = False
lives = 5
print("I've the number between 1-" + str(range_user) + ". You have " + str(lives) + " lives.")

while lives > 0 and not win:
    right_guess = False
    while not right_guess:
        guess = input("Make your guess: ")
        right_guess = guess.isnumeric()
    if int(guess) == r:
        win = True
        print("Congratulations!")
    if int(guess) > r:
        lives -= 1
        if lives == 0:
            print("You are dead!")
        else:
            print("Too high, you have " + str(lives) + " lives left.")
    if int(guess) < r:
        lives -= 1
        if lives == 0:
            print("You are dead!")
        else:
            print("Too low, you have " + str(lives) + " lives left.")





