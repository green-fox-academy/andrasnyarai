# Write a program that stores 3 sides of a cuboid as variables (doubles)
# The program should write the surface area and volume of the cuboid like:
# 
# Surface Area: 600
# Volume: 1000
a = 10
b = 10
c = 10

Surface = ((a * b) + (b * c) + (c * a)) * 2
Volume = a * b * c
print("Surface Area: " + str(Surface))
print("Volume: "+ str(Volume))
