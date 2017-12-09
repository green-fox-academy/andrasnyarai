from tkinter import *
root = Tk()

SIZE = 600

canvas = Canvas(root, width=SIZE, height=SIZE, bg="#f0fff0")
canvas.pack()


def sierpinski_carpet(d,x,y,size):
    if d < 1:
        return
    canvas.create_rectangle(x,y,x + size,y + size, fill="black", outline="white")

    sierpinski_carpet(d-1,x,y,size)

    m = size/3

    sierpinski_carpet(d-1,x - size*2/3,y - 2*m, m)
    sierpinski_carpet(d-1,x - size*2/3,y + m, m)
    sierpinski_carpet(d-1,x - size*2/3,y + 4*m, m)

    sierpinski_carpet(d-1,x + m,y - 2*m , m)
    sierpinski_carpet(d-1,x + m,y + 4*m , m)

    sierpinski_carpet(d-1,x + 2*2/3*size,y - 2*m, m)
    sierpinski_carpet(d-1,x + 2*2/3*size,y + m, m)
    sierpinski_carpet(d-1,x + 2*2/3*size,y + 4*m, m)


sierpinski_carpet(5,200,200,200)

root.mainloop()