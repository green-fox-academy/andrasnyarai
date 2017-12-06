from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]


a = "blue"
b = "red"

def drawing_lines(x,y,w,z,q):
    my_line = canvas.create_line(x,y,w,z,fill=q)


for i in range(0, 301, 20):    
    drawing_lines(0,i,i,300,a)
    drawing_lines(i,0,300,i,b)




root.mainloop()
