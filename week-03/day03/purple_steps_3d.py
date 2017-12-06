from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps-3d/r4.png]

def purple_blocks(x,y):
    initial_block = canvas.create_rectangle(x,x,y,y, fill="purple")



a = 2
x = 3
for o in range(2,7):
    purple_blocks((x*(a**o)),(x*(a**(o+1))))

root.mainloop()

