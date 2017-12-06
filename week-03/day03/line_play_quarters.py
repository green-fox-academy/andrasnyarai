from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# divide the canvas into 4 equal parts
# and repeat this pattern in each quarter:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]


a = "olive"

def drawing_lines(x,y,w,z,q):
    my_line = canvas.create_line(x,y,w,z,fill=q)


for i in range(0, 150, 10):    
    drawing_lines(0,150+i,i,300,a)
    drawing_lines(150+i,300,300,300-i,a)
    drawing_lines(300,150-i,300-i,0,a)
    drawing_lines(150-i,0,0,i,a)





root.mainloop()
