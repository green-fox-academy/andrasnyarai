from tkinter import *
from math import *

root = Tk()

size = 600

canvas = Canvas(root, width=size, height=size, bg="white")
canvas.pack()

def koch_snow(depth, x0, y0, size):
    if depth == 5:
        return

    length = sqrt(size**2 - (size/2)**2)

    canvas.create_polygon(x0,
    y0,
    x0 - size/2,
    y0 - length,
    x0 + size/2,
    y0 - length,
    fill="black")
    canvas.create_polygon(x0,
    y0 - length - length/3,
    x0 - size/2,
    y0 - length/3,
    x0 + size/2,
    y0 - length/3,
    fill="black")

    koch_snow(depth+1,x0 ,y0,size/3)

    koch_snow(depth+1,x0,y0 - length*7.1/8,size/3)

    koch_snow(depth+1,x0 + size/3, y0 - length*10.7/16, size/3)

    koch_snow(depth+1,x0 - size/3, y0 - length*10.7/16, size/3)

    koch_snow(depth+1,x0 - size/3, y0 - length*3.6/16, size/3)

    koch_snow(depth+1,x0 + size/3, y0 - length*3.6/16, size/3)


koch_snow(1,300,450,300)

def plus():
    print('helo')
    root.after(5000,plus)


root.after('5000',plus)
root.mainloop()