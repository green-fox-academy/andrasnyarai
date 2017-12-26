from tkinter import *

root = Tk()
SIZE = 600
canvas = Canvas(root, width=SIZE, height=SIZE, bg="white")
canvas.pack()

class H_tree(object):

    def __init__(self):
        self.depth = 0

    def h_tree(self, depth, x, y, length):
        if depth == 0:
            return

        canvas.create_line(x, y, x + length, y, width=depth, fill="purple")
        canvas.create_line(x, y - length/2, x, y + length/2, width=depth, fill="purple")
        canvas.create_line(x + length, y - length/2, x + length, y + length/2, width=depth, fill="purple")

        self.h_tree(depth - 1, x - length/4, y - length/2, length/2)
        self.h_tree(depth - 1, x - length/4, y + length/2, length/2)
        self.h_tree(depth - 1, x + length*3/4, y - length/2, length/2)
        self.h_tree(depth - 1, x + length*3/4, y + length/2, length/2)

h_tree = H_tree()

def on_key_press(e):

    if e.keysym == "Return":
        h_tree.depth = 0    
        print(h_tree.depth)
        canvas.create_rectangle(0,0,SIZE,SIZE, fill="white")

    elif e.keysym == "space":
        h_tree.depth += 1
        print(h_tree.depth)
        h_tree.h_tree(h_tree.depth,150,300,300)

    elif e.keysym == "minus":
        if h_tree.depth == 0:
            return
        h_tree.depth -= 1
        print(h_tree.depth)
        canvas.create_rectangle(0,0,SIZE,SIZE, fill="white")
        h_tree.h_tree(h_tree.depth,150,300,300)

root.update_idletasks()

canvas.bind("<KeyPress>", on_key_press)
canvas.focus_set()

root.mainloop()