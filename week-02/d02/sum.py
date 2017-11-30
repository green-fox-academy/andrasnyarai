# - Write a function called `sum` that sum all the numbers
#   until the given parameter
def sum(x):
    s = 0
    for i in range(1,x+1):
        s = s + i
    return s
x = int(input())
print(sum(x))