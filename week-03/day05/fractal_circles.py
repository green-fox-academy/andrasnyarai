from tkinter import *

root = Tk()

SIZE = 600

canvas = Canvas(root, width=SIZE, height=SIZE, bg="#f0fff0")
canvas.pack()


def drawcircle(d,x,y,r):
    if d < 4:
        return
    canvas.create_oval(x,y, x + r*2, y + r*2, outline="black")

    u = r/18

    drawcircle(d-1,
     x +r/2,
     y,
     1/2*r)
    drawcircle(d-1,
     x + u,
     y + r*2/3 + u,
     1/2*r)
    drawcircle(d-1,
     x + r - u,
     y + r*2/3 + u,
     1/2*r)


drawcircle(8,2,2,298)


root.mainloop()