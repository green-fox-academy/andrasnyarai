from tkinter import *
from math import *

root = Tk()

size = 600

canvas = Canvas(root, width=size, height=size, bg="black")
canvas.pack()

def koch_snow(depth,x0, y0, size):
    if depth == 5:
        return

    length = sqrt(size**2 - (size/2)**2)

    canvas.create_polygon(x0,
    y0,
    x0 - size/2,
    y0 - length,
    x0 + size/2,
    y0 - length,
    fill="white")
    canvas.create_polygon(x0,
    y0 - length - length/3,
    x0 - size/2,
    y0 - length/3,
    x0 + size/2,
    y0 - length/3,
    fill="white")

    koch_snow(depth+1,x0 ,y0,size/3)

    koch_snow(depth+1,x0,y0 - length*7/8,size/3)

    koch_snow(depth+1,x0 + size/3, y0 - length*11/16, size/3)

    koch_snow(depth+1,x0 - size/3, y0 - length*11/16, size/3)

    koch_snow(depth+1,x0 - size/3, y0 - length*3.5/16, size/3)

    koch_snow(depth+1,x0 + size/3, y0 - length*3.5/16, size/3)



koch_snow(1,300,450,300)

root.mainloop()








'''     if (depth <= 0):
        canvas.create_polygon(x0, y0, x1, y1, x2, y2, fill="#ff69b4", outline="#3a3a3a", width="0.5")
    else:
        drawSierpinski(depth-1,x0,y0,average(x0,x1), average(y0,y1),average(x0,x2), average(y0,y2))
        drawSierpinski(depth-1,average(x0,x1), average(y0,y1),x1, y1,average(x1,x2), average(y1, y2))
        drawSierpinski(depth-1,average(x0,x2), average(y0,y2),average(x1,x2), average(y1, y2),x2, y2) '''