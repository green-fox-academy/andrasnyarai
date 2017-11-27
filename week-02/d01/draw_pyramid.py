# Write a program that reads a number from the standard input, then draws a
# pyramid like this:
#
#
#    *
#   ***
#  *****
# *******
#
# The pyramid should have as many lines as the number was
t = input("Number: ")
a = 0
while a <= int(t):
  print((int(t)-a)*" ", a*"*" + (a-1)*"*")
  a += 1