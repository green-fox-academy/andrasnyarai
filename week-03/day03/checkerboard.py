from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# fill the canvas with a checkerboard pattern.

cell_size = 30

for i in range(0,10):
    for j in range(0,10):
        if (i + j) % 2 == 0:
            board = canvas.create_rectangle((i * cell_size)+2,(j * cell_size)+2,((i+1)*cell_size),((j+1)*cell_size), fill="black")
        else:
            board = canvas.create_rectangle((i * cell_size)+2,(j * cell_size)+2,((i+1)*cell_size),((j+1)*cell_size), fill="white")



root.mainloop()
