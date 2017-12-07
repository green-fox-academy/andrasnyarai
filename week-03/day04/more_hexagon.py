from tkinter import *

root = Tk()

canvas = Canvas(root, width='600', height='600')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/super-hexagon/r6.gif]


q = 0  # q - is for to adjust the right half of the structure, when n is counting down
n = 0
Ascend = True
multiplication = 4

# hexa value default 10
sidex = 10
sidey = 10

for x in range(9):
    s = 50*n + q*50
    h = -(n*40)  
    for i in range(multiplication):
        poly = canvas.create_polygon((4*sidex)+s,(21*sidey)-h,(5*sidex)+s,(23*sidey)-h,(7*sidex)+s,(23*sidey)-h,(8*sidex)+s,(21*sidey)-h,(7*sidex)+s,(19*sidey)-h,(5*sidex)+s,(19*sidey)-h, fill="white", outline="black")
        h += 4*sidey
    n += 1

    if multiplication == 8:
        Ascend = False
        q = 0

    if Ascend is False:
        multiplication -= 1
        q += 2
        n -=2

    if Ascend is True:
        multiplication += 1
        s = 0
        h = 0


root.mainloop()
