from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/triangles/r5.png]
l = 17
m = 10
rd = 20







for i in range(20,260-(0*rd),20):
    move = canvas.create_line(20+(0*m)+i,236+(0*l),30+(0*m)+i,253+(0*l))
    move = canvas.create_line(30+(0*m)+i,253+(0*l),10+(0*m)+i,253+(0*l))
    move = canvas.create_line(10+(0*m)+i,253+(0*l),20+(0*m)+i,236+(0*l))

for i in range(20,260-rd,20):
    move = canvas.create_line(20+m+i,236-l,30+m+i,253-l)
    move = canvas.create_line(30+m+i,253-l,10+m+i,253-l)
    move = canvas.create_line(10+m+i,253-l,20+m+i,236-l)

for i in range(20,260-rd-rd,20):
    move = canvas.create_line(20+m+m+i,236-l-l,30+m+m+i,253-l-l)
    move = canvas.create_line(30+m+m+i,253-l-l,10+m+m+i,253-l-l)
    move = canvas.create_line(10+m+m+i,253-l-l,20+m+m+i,236-l-l)

for i in range(20,260-rd-rd-rd,20):
    move = canvas.create_line(20+m+m+m+i,236-l-l-l,30+m+m+m+i,253-l-l-l)
    move = canvas.create_line(30+m+m+m+i,253-l-l-l,10+m+m+m+i,253-l-l-l)
    move = canvas.create_line(10+m+m+m+i,253-l-l-l,20+m+m+m+i,236-l-l-l)

for i in range(20,260-rd-rd-rd-rd,20):
    move = canvas.create_line(20+m+m+m+m+i,236-l-l-l-l,30+m+m+m+m+i,253-l-l-l-l)
    move = canvas.create_line(30+m+m+m+m+i,253-l-l-l-l,10+m+m+m+m+i,253-l-l-l-l)
    move = canvas.create_line(10+m+m+m+m+i,253-l-l-l-l,20+m+m+m+m+i,236-l-l-l-l)

for i in range(20,260-rd-rd-rd-rd-rd,20):
    move = canvas.create_line(20+m+m+m+m+m+i,236-l-l-l-l-l,30+m+m+m+m+m+i,253-l-l-l-l-l)
    move = canvas.create_line(30+m+m+m+m+m+i,253-l-l-l-l-l,10+m+m+m+m+m+i,253-l-l-l-l-l)
    move = canvas.create_line(10+m+m+m+m+m+i,253-l-l-l-l-l,20+m+m+m+m+m+i,236-l-l-l-l-l)

for i in range(20,260-rd-rd-rd-rd-rd-rd,20):
    move = canvas.create_line(20+m+m+m+m+m+m+i,236-l-l-l-l-l-l,30+m+m+m+m+m+m+i,253-l-l-l-l-l-l)
    move = canvas.create_line(30+m+m+m+m+m+m+i,253-l-l-l-l-l-l,10+m+m+m+m+m+m+i,253-l-l-l-l-l-l)
    move = canvas.create_line(10+m+m+m+m+m+m+i,253-l-l-l-l-l-l,20+m+m+m+m+m+m+i,236-l-l-l-l-l-l)

for i in range(20,260-rd-rd-rd-rd-rd-rd-rd,20):
    move = canvas.create_line(20+m+m+m+m+m+m+m+i,236-l-l-l-l-l-l-l,30+m+m+m+m+m+m+m+i,253-l-l-l-l-l-l-l)
    move = canvas.create_line(30+m+m+m+m+m+m+m+i,253-l-l-l-l-l-l-l,10+m+m+m+m+m+m+m+i,253-l-l-l-l-l-l-l)
    move = canvas.create_line(10+m+m+m+m+m+m+m+i,253-l-l-l-l-l-l-l,20+m+m+m+m+m+m+m+i,236-l-l-l-l-l-l-l)

for i in range(20,260-rd-rd-rd-rd-rd-rd-rd-rd,20):
    move = canvas.create_line(20+m+m+m+m+m+m+m+m+i,236-l-l-l-l-l-l-l-l,30+m+m+m+m+m+m+m+m+i,253-l-l-l-l-l-l-l-l)
    move = canvas.create_line(30+m+m+m+m+m+m+m+m+i,253-l-l-l-l-l-l-l-l,10+m+m+m+m+m+m+m+m+i,253-l-l-l-l-l-l-l-l)
    move = canvas.create_line(10+m+m+m+m+m+m+m+m+i,253-l-l-l-l-l-l-l-l,20+m+m+m+m+m+m+m+m+i,236-l-l-l-l-l-l-l-l)

for i in range(20,260-rd-rd-rd-rd-rd-rd-rd-rd-rd,20):
    move = canvas.create_line(20+m+m+m+m+m+m+m+m+m+i,236-l-l-l-l-l-l-l-l-l,30+m+m+m+m+m+m+m+m+m+i,253-l-l-l-l-l-l-l-l-l)
    move = canvas.create_line(30+m+m+m+m+m+m+m+m+m+i,253-l-l-l-l-l-l-l-l-l,10+m+m+m+m+m+m+m+m+m+i,253-l-l-l-l-l-l-l-l-l)
    move = canvas.create_line(10+m+m+m+m+m+m+m+m+m+i,253-l-l-l-l-l-l-l-l-l,20+m+m+m+m+m+m+m+m+m+i,236-l-l-l-l-l-l-l-l-l)

for i in range(20,260-rd-rd-rd-rd-rd-rd-rd-rd-rd-rd,20):
    move = canvas.create_line(20+m+m+m+m+m+m+m+m+m+m+i,236-l-l-l-l-l-l-l-l-l-l,30+m+m+m+m+m+m+m+m+m+m+i,253-l-l-l-l-l-l-l-l-l-l)
    move = canvas.create_line(30+m+m+m+m+m+m+m+m+m+m+i,253-l-l-l-l-l-l-l-l-l-l,10+m+m+m+m+m+m+m+m+m+m+i,253-l-l-l-l-l-l-l-l-l-l)
    move = canvas.create_line(10+m+m+m+m+m+m+m+m+m+m+i,253-l-l-l-l-l-l-l-l-l-l,20+m+m+m+m+m+m+m+m+m+m+i,236-l-l-l-l-l-l-l-l-l-l)

for i in range(20,260-rd-rd-rd-rd-rd-rd-rd-rd-rd-rd-rd,20):
    move = canvas.create_line(20+m+m+m+m+m+m+m+m+m+m+m+i,236-l-l-l-l-l-l-l-l-l-l-l,30+m+m+m+m+m+m+m+m+m+m+m+i,253-l-l-l-l-l-l-l-l-l-l-l)
    move = canvas.create_line(30+m+m+m+m+m+m+m+m+m+m+m+i,253-l-l-l-l-l-l-l-l-l-l-l,10+m+m+m+m+m+m+m+m+m+m+m+i,253-l-l-l-l-l-l-l-l-l-l-l)
    move = canvas.create_line(10+m+m+m+m+m+m+m+m+m+m+m+i,253-l-l-l-l-l-l-l-l-l-l-l,20+m+m+m+m+m+m+m+m+m+m+m+i,236-l-l-l-l-l-l-l-l-l-l-l)







root.mainloop()
