from tkinter import *
import random

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

def styling_box(size,color):
    x1 = 0 + size/2
    x2 = 300 - size/2
    y1 = 0 + size/2
    y2 = 300 - size/2
    center_box = canvas.create_rectangle(x1,y1,x2,y2,fill=color)


for i in range(0, 300, 15):
    colorval = "#%02x%02x%02x" % (random.randrange(0,255), random.randrange(0,255), random.randrange(0,255))
    styling_box(i,colorval)

# I need to figure out how to refresh canvas with new random numbers for color

root.mainloop()
