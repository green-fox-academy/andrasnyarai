from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a function that takes 1 parameter:
# a list of [x, y] points
# and connects them with green lines.
# connect these to get a box: [[10, 10], [290,  10], [290, 290], [10, 290]]
# connect these: [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
# [120, 100], [85, 130], [50, 100]]
a = [[10, 10], [290,  10], [290, 290], [10, 290]]
b = [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70], [120, 100], [85, 130], [50, 100]]




def connect(parameters):
    for u in range(1, len(parameters)):
        my_lines = canvas.create_line(parameters[u-1][0],parameters[u-1][1],parameters[u][0],parameters[u][1])
    my_lines = canvas.create_line(parameters[0][0],parameters[0][1],parameters[len(parameters)-1][0],parameters[len(parameters)-1][1])

connect(a)
connect(b)

root.mainloop()
