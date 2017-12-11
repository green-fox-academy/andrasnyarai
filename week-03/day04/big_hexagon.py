from tkinter import *
from math import *
root = Tk()

SIZE = 600

canvas = Canvas(root, width=SIZE, height=SIZE, bg="#f0fff0")
canvas.pack()

def drawhexa(d,x,y,size):
    h = sqrt(size**2 - (size/2)**2)
    if d < 1:
        return
    
    canvas.create_polygon(x,y,
    x + size/2, y - h,
    x + 3/2 * size, y - h,
    x + 2 * size, y,
    x + 3/2 * size, y + h,
    x + size/2, y + h, fill="black", outline="white")

    drawhexa(d-1,
    x + size/4,
    y - h/2,
    size/2)
    drawhexa(d-1,
    x + size,
    y,
    size/2)
    drawhexa(d-1,
    x + size/4,
    y + h/2,
    size/2)

drawhexa(6,5,300,298)

root.mainloop()