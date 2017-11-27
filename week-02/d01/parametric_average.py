# Write a program that asks for a number.
# It would ask this many times to enter an integer,
# if all the integers are entered, it should print the sum and average of these
# integers like:
#
# Sum: 22, Average: 4.4
x = input("Feed the machine a number: ")
y = input("Feed the machine a number: ")
w = input("Feed the machine a number: ")
z = input("Feed the machine a number: ")
q = input("Feed the machine a number: ")
p = input("Feed the machine a number: ")
sum = x+y+w+z+q+p
sum = int(sum)
ave = sum/6
print("Sum: "+ str(sum) + " Average: "+ str(ave))