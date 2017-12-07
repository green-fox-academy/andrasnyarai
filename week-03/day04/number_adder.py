# Write a recursive function that takes one parameter: n and adds numbers from 1 to n.

def adder(number):
    if number <= 1:
        return 1
    else:
        return number + adder(number-1)


print(adder(4))