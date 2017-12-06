from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.

def centered(size):
    x1 = 0 + size/2
    x2 = 300 - size/2
    y1 = 0 + size/2
    y2 = 300 - size/2
    center_box = canvas.create_rectangle(x1,y1,x2,y2)

centered(225)
centered(200)
centered(175)

root.mainloop()
