from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a 50 long horizontal line from that point.
# draw 3 lines with that function.

def horizontal_line(x,y):
    my_lines = canvas.create_line(x,y,x+50,y)

horizontal_line(25,25)
horizontal_line(75,75)
horizontal_line(125,125)

root.mainloop()