from tkinter import *
root = Tk()

SIZE = 600

canvas = Canvas(root, width=SIZE, height=SIZE, bg="#f0fff0")
canvas.pack()

def grid(d,x,y,size):
    if d < 1:
        return

    canvas.create_rectangle(x,y,x + size,y + size, width=str(size/15))

    grid(d-1,x - size/4,y - size/4,size/2)
    grid(d-1,x + size*3/4,y - size/4,size/2)
    grid(d-1,x - size/4,y + size*3/4,size/2)
    grid(d-1,x + size*3/4,y + size*3/4,size/2)

grid(5,150,150,300)

root.mainloop()