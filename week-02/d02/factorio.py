# - Create a function called `factorio`
#   that returns it's input's factorial
def factorio(x):
    s = 1
    for i in range(1,x+1):
        s = s * i
    return s
x = int(input())
print(sum(x))