from tkinter import *
from math import *

root = Tk()



canvas = Canvas(root, width=1200, height=600, bg="#7FFFBF")
canvas.pack()

length = 100


def first_line(depth, x0,y0,angle):
    if depth < 2:
        return
    x1 = x0 + int(cos(radians(angle)) * 4/5*depth * 10)
    y1 = y0 + int(sin(radians(angle)) * 4/5*depth * 10)
    initial = canvas.create_line(x0,y0/2,x1,y1/2, fill="#444", width="0.7")


    first_line(depth-1,
    x1,
    y1,
    angle - 10,)

    first_line(depth-1,
    x1,
    y1,
    angle + 10,)





first_line(15,600,1200,-90)



root.mainloop()