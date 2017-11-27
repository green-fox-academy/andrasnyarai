# Create a program that asks for two numbers
# If the second number is not bigger than the first one it should print:
# "The second number should be bigger"
#
# If it is bigger it should count from the first number to the second by one
# 
# example:
#
# first number: 3, second number: 6, should print:
#
# 3
# 4
# 5
fir = input("number#1: ")
sec = input("number#2: ")
if sec <= fir:
    print("The second number should be bigger")
elif fir < sec:
    for i in range(fir, sec, 1):
    print(i)
