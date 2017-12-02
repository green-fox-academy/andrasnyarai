# palindrome

string = "from the mountain"

def create_palindrome(x):
    y = list(x)
    z = reversed(y)
    w = ''.join(z)
    return x + w

print(create_palindrome(string))