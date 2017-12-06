from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps-3d/r4.png]

a = 5
b = 15
growth = 10
for i in range(6):
    steps = canvas.create_rectangle(a,a,b,b, fill="purple")
    a += growth
    growth += 10
    b += growth

root.mainloop()
