from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# draw 3 lines with that function.

def drawing_lines(x,y):
    my_line = canvas.create_line(x,y,150,150)

drawing_lines(10,10)
drawing_lines(200,200)
drawing_lines(150,0)

root.mainloop()
