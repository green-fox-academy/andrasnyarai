# Write a program that asks for 5 integers in a row,
# then it should print the sum and the average of these numbers like:
#
# Sum: 22, Average: 4.4
a = input("first number: ")
b = input("second number: ")
c = input("third number: ")
d = input("fourth number: ")
e = input("last number: ")

sum = int(a) + int(b) + int(c) + int(d) + int(e)
ave = sum / 5

print("Sum: " + str(sum)+ "," + " Average: " + str(ave))