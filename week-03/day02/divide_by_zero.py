# create a function that takes a number,
# divides ten with it,
# and prints the result.
# it should print "fail" if the parameter is 0

number = 0

def divide(num):
    try:
        x = 10 / num
        print(x)
    except ZeroDivisionError:
        print("fail")

divide(number)