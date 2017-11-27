# Write a program that reads a number from the standard input, then draws a
# triangle like this:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as the number was
t = input("Number: ")
a = 0
while a <= int(t):
  print(a*"*")
  a += 1