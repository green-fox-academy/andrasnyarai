from tkinter import *

root = Tk()
SIZE = 600
canvas = Canvas(root, width=SIZE, height=SIZE, bg="white")
canvas.pack()

def h_tree(depth, x, y, length):
    if depth == 0:
        return

    canvas.create_line(x, y, x + length, y, width=depth, fill="purple")
    canvas.create_line(x, y - length/2, x, y + length/2, width=depth, fill="purple")
    canvas.create_line(x + length, y - length/2, x + length, y + length/2, width=depth, fill="purple")

    h_tree(depth - 1, x - length/4, y - length/2, length/2)
    h_tree(depth - 1, x - length/4, y + length/2, length/2)
    h_tree(depth - 1, x + length*3/4, y - length/2, length/2)
    h_tree(depth - 1, x + length*3/4, y + length/2, length/2)

h_tree(5, 150, 300, 300)

root.mainloop()