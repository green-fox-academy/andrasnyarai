# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
# %%%%%
# %   %
# %   %
# %   %
# %   %
# %%%%%
#
# The square should have as many lines as the number was
t = input("Number: ")
a = 0
while a <= int(t):
  print(t*"%")
  a += 1