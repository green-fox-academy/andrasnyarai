from tkinter import *
from math import *
import random

root = Tk()
canvas = Canvas(root, width=600, height=600)
canvas.pack()

class Walker(object):

    def __init__(self):
        self.depth = 0

    def random_walk(self, depth, x, y, length):
        if depth == 0:
            return

        a = random.choice([0, 180, 90, -90])

        angle_in_radians = a * pi / 180
        x1 = x + length * cos(angle_in_radians)
        y1 = y + length * sin(angle_in_radians)

        canvas.create_line(x, y, x1, y1)

        self.random_walk(depth - 1, x1, y1, length)

w = Walker()

def on_key_press(e):

    if e.keysym == "Return":
        w.depth += 1
        print(w.depth)

    elif e.keysym == "space":
        canvas.create_rectangle(0, 0, 600, 600, fill="white", outline="white")
        w.random_walk(w.depth, 300, 300, 20)
        print(w.depth)

    elif e.keysym == "minus":
        w.depth -= 1
        print(w.depth)

root.update_idletasks()

canvas.bind("<KeyPress>", on_key_press)
canvas.focus_set()

root.mainloop()