# palindrome

string = "Mountain and the river"

def turn(x):
    y = list(x)
    z = reversed(y)
    w = ''.join(z)
    return w

print(turn(string))