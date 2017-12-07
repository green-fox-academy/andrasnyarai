from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/super-hexagon/r6.gif]


q = 0  # q - is for to adjust the right half of the structure, when n is counting down
n = 0
Ascend = True
multiplication = 4

for x in range(7):
    s = 30*n + q*30
    h = -(n*20)  
    for i in range(multiplication):
        poly = canvas.create_polygon(40+s,210-h,50+s,230-h,70+s,230-h,80+s,210-h,70+s,190-h,50+s,190-h, fill="white", outline="black")
        h += 40
    n += 1

    if multiplication == 7:
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
