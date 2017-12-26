from tkinter import *

root = Tk()
SIZE = 600
width = SIZE*2
height = SIZE *4/5
canvas = Canvas(root, width=width, height=height, bg="#db132b")
canvas.pack()

class Cantor_set(object):

    def __init__(self):
        self.depth = 0

    def cantor_set(self, depth, x, y, length, offset):
        if depth == 0:
            return

        canvas.create_line(x, y, x + length, y, width=20)

        self.cantor_set(depth - 1, x, y + offset, length/3, offset)

        self.cantor_set(depth - 1, x + length*2/3, y + offset, length/3, offset)

cantor_set = Cantor_set()

def on_key_press(e):

    if e.keysym == "Return":
        cantor_set.depth = 0    
        print(cantor_set.depth)
        canvas.create_rectangle(0,0,width,height, fill="#db132b")

    elif e.keysym == "space":
        cantor_set.depth += 1
        print(cantor_set.depth)
        cantor_set.cantor_set(cantor_set.depth, 50, 50, 1100, 50)

    elif e.keysym == "minus":
        if cantor_set.depth == 0:
            return
        cantor_set.depth -= 1
        print(cantor_set.depth)
        canvas.create_rectangle(0,0,width,height, fill="#db132b")
        cantor_set.cantor_set(cantor_set.depth, 50, 50, 1100, 50)

root.update_idletasks()

canvas.bind("<KeyPress>", on_key_press)
canvas.focus_set()

root.mainloop()
