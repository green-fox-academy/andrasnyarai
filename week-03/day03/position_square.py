from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the x and y coordinates of the square's top left corner
# and draws a 50x50 square from that point.
# draw 3 squares with that function.

def square_draw(x,y):
    my_box = canvas.create_rectangle(x,y,x+50,y+50)

square_draw(75,75)
square_draw(125,125)
square_draw(175,175)

root.mainloop()
