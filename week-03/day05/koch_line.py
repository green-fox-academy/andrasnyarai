from tkinter import *
from math import *

root = Tk()

canvas = Canvas(root, width=600, height=600, bg="white")
canvas.pack()


def lines(depth,x0,y0,size):
    if depth == 1:
        return
    length = sqrt((size)**2 - (size/2)**2)


    canvas.create_line(x0,y0,x0 + size, y0)
    canvas.create_line(x0 + size, y0, x0 + size + size/2,y0 - length)
    canvas.create_line(x0 + size + size/2, y0 - length, x0 + 2*size, y0)
    canvas.create_line(x0 + 2*size, y0, x0 + 3*size, y0)
    canvas.create_line(x0 + size, y0, x0 + 2*size, y0,fill="white")

    canvas.create_line(x0 + size, y0 - length*2/3, x0 + size + size/2*(2/3),y0 - length*2/3)
    canvas.create_line(x0 + size, y0 - length*2/3, x0 + size + size/2*(1/3),y0 - length*1/3)
    canvas.create_line(x0 + size + size/2*(2/3),y0 - length*2/3,x0 + size + size/2*(1/3),y0 - length*1/3,fill="white",width="2")

    canvas.create_line(x0 + size + size/2 + size/2*(1/3),y0 - length*2/3, x0 + 2*size, y0 - length*2/3)
    canvas.create_line(x0 + size + size/2 + size/2*(2/3),y0 - length*1/3, x0 + 2*size, y0 - length*2/3)
    canvas.create_line(x0 + size + size/2 + size/2*(1/3),y0 - length*2/3,x0 + size + size/2 + size/2*(2/3),y0 - length*1/3, fill="white", width="2")


    lines(depth-1,x0,y0,size/3)
    lines(depth-1,x0 + 2*size,y0,size/3)

 




lines(10,0,500,200)

root.mainloop()