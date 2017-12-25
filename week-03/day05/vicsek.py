from tkinter import *

root = Tk()
SIZE = 600
canvas = Canvas(root, width=SIZE, height=SIZE, bg="#532493")
canvas.pack()

def vicsek(depth, xa, ya, size):
    if depth == 0:
        return

    canvas.create_rectangle(xa, ya, xa + size, ya + size, fill="white", outline="white")
    canvas.create_rectangle(xa + 2*size, ya, xa + 3*size, ya + size, fill="white", outline="white")
    canvas.create_rectangle(xa, ya + 2*size,xa + size, ya + 3*size, fill="white", outline="white")
    canvas.create_rectangle(xa + 2*size,ya + 2*size,xa + 3*size, ya + 3*size, fill="white", outline="white")

    vicsek(depth - 1, xa + size, ya, size/3)
    vicsek(depth - 1, xa + 2*size, ya + size, size/3)
    vicsek(depth - 1, xa + size, ya + 2*size, size/3)
    vicsek(depth - 1, xa, ya + size, size/3)
    vicsek(depth - 1, xa + size, ya + size, size/3)

vicsek(5,1,1,SIZE/3)
root.mainloop()