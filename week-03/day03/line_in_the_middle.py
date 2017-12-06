from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

canvas.line(0, 150, 0, 150, fill="red")
# draw a red horizontal line to the canvas' middle.
# draw a green vertical line to the canvas' middle.

root.mainloop()
