from tkinter import *

root = Tk()
SIZE = 600
canvas = Canvas(root, width=SIZE*2, height=SIZE *4/5, bg="#db132b")
canvas.pack()

def cantor_set(depth, x, y, length, offset):
    if depth == 0:
        return

    canvas.create_line(x, y, x + length, y, width=20)

    cantor_set(depth - 1, x, y + offset, length/3, offset)

    cantor_set(depth - 1, x + length*2/3, y + offset, length/3, offset)


cantor_set(7, 50, 50, 1100, 50)

root.mainloop()
