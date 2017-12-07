from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/super-hexagon/r6.gif]

s = 0
h = 0
for i in range(4):
    poly = canvas.create_polygon(40+s,210-h,50+s,230-h,70+s,230-h,80+s,210-h,70+s,190-h,50+s,190-h, fill="white", outline="black")
    h += 40

s = 30
h = 0 - 20
for i in range(5):
    poly = canvas.create_polygon(40+s,210-h,50+s,230-h,70+s,230-h,80+s,210-h,70+s,190-h,50+s,190-h, fill="white", outline="black")
    h += 40

s = 30 + 30
h = 0 - 20 - 20
for i in range(6):
    poly = canvas.create_polygon(40+s,210-h,50+s,230-h,70+s,230-h,80+s,210-h,70+s,190-h,50+s,190-h, fill="white", outline="black")
    h += 40

s = 30 + 30 + 30
h = 0 - 20 - 20 - 20
for i in range(7):
    poly = canvas.create_polygon(40+s,210-h,50+s,230-h,70+s,230-h,80+s,210-h,70+s,190-h,50+s,190-h, fill="white", outline="black")
    h += 40

s = 30 + 30 + 30 + 30
h = 0 - 20 - 20
for i in range(6):
    poly = canvas.create_polygon(40+s,210-h,50+s,230-h,70+s,230-h,80+s,210-h,70+s,190-h,50+s,190-h, fill="white", outline="black")
    h += 40

s = 30 + 30 + 30 + 30 + 30
h = 0 - 20
for i in range(5):
    poly = canvas.create_polygon(40+s,210-h,50+s,230-h,70+s,230-h,80+s,210-h,70+s,190-h,50+s,190-h, fill="white", outline="black")
    h += 40

s = 30 + 30 + 30 + 30 + 30 + 30     #horizontal adjust
h = 0                               #vertical adjust & multiplication
for i in range(4):
    poly = canvas.create_polygon(40+s,210-h,50+s,230-h,70+s,230-h,80+s,210-h,70+s,190-h,50+s,190-h, fill="white", outline="black")
    h += 40

root.mainloop()