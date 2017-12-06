from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

def drawing_lines(x,y):
    my_line = canvas.create_line(x,y,150,150)


for i in range(0, 301, 20):    
    drawing_lines(0,i)
for i in range(0, 301, 20):    
    drawing_lines(i,300)
for i in range(0, 301, 20):    
    drawing_lines(300,i)
for i in range(0, 301, 20):    
    drawing_lines(i,0)




root.mainloop()
