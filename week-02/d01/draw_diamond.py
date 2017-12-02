# Write a program that reads a number from the standard input, then draws a
# diamond like this:
#
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# The diamond should have as many lines as the number was
t = input("Number: ")
a = 0
l = " "
t = (int(t)/2) + 1
while a <= int(t):
  print((int(t)-a)*l, a*"*" + (a-1)*"*")
  a += 1
a = 0
while a <= int(t):
  print(l + a*l, (int(t)-a-1)*"*" + ((int(t)-a-1)-1)*"*")
  a += 1