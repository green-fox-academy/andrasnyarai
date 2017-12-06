from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/envelope-star/r2.png]

a = "pink"

def drawing_lines(x,y,w,z,q):
    my_line = canvas.create_line(x,y,w,z,fill=q)


for i in range(0, 150, 10):    
    drawing_lines(i,150,150,150+i,a)
    drawing_lines(150,300-i,150+i,150,a)
    drawing_lines(300-i,150,150,150-i,a)
    drawing_lines(150,i,150-i,150,a)





root.mainloop()
