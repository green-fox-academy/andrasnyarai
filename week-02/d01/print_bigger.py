# Write a program that asks for two numbers and prints the bigger one
a = input("number_1: ")
b = input("number_2: ")

if int(a) > int(b):
    print(a)
elif int(b) > int(a):
    print(b)