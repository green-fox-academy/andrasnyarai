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


a = input("give me a number: ")
a = int(a)
i = 1
print(a*"%")
while i <= a-2:
    print("%" + (a-2)*" " + "%")
    i += 1
print(a*"%")
