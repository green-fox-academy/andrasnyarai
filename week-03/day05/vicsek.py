from tkinter import *

root = Tk()
SIZE = 600
canvas = Canvas(root, width=SIZE, height=SIZE, bg="#532493")
canvas.pack()

class Vicsek(object):

    def __init__(self):
        self.depth = 0

    def vicsek(self, depth, xa, ya, size):
        if depth == 0:
            return

        canvas.create_rectangle(xa, ya, xa + size, ya + size, fill="white", outline="white")
        canvas.create_rectangle(xa + 2*size, ya, xa + 3*size, ya + size, fill="white", outline="white")
        canvas.create_rectangle(xa, ya + 2*size,xa + size, ya + 3*size, fill="white", outline="white")
        canvas.create_rectangle(xa + 2*size,ya + 2*size,xa + 3*size, ya + 3*size, fill="white", outline="white")

        self.vicsek(depth - 1, xa + size, ya, size/3)
        self.vicsek(depth - 1, xa + 2*size, ya + size, size/3)
        self.vicsek(depth - 1, xa + size, ya + 2*size, size/3)
        self.vicsek(depth - 1, xa, ya + size, size/3)
        self.vicsek(depth - 1, xa + size, ya + size, size/3)

vicsek = Vicsek()

def on_key_press(e):

    if e.keysym == "Return":
        vicsek.depth = 0    
        print(vicsek.depth)
        canvas.create_rectangle(0,0,SIZE,SIZE, fill="#532493")

    elif e.keysym == "space":
        vicsek.depth += 1
        print(vicsek.depth)
        vicsek.vicsek(vicsek.depth,1,1,SIZE/3)

    elif e.keysym == "minus":
        if vicsek.depth == 0:
            return
        vicsek.depth -= 1
        print(vicsek.depth)
        canvas.create_rectangle(0,0,SIZE,SIZE, fill="#532493")
        vicsek.vicsek(vicsek.depth,1,1,SIZE/3)

root.update_idletasks()

canvas.bind("<KeyPress>", on_key_press)
canvas.focus_set()

root.mainloop()
