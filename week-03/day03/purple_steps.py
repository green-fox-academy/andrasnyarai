from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps/r3.png]

def purple_blocks(x,y):
    initial_block = canvas.create_rectangle(x,y,x+10,y+10, fill="purple")

for i in range(10, 200, 10):
    purple_blocks(i,i)




root.mainloop()
