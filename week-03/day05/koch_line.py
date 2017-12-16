from tkinter import *
from math import *

root = Tk()

canvas = Canvas(root, width='600', height='600',bg="white")
canvas.pack()

def lines(depth, x, y, length, a, b, c, d):
    if depth == 1:
        return

    angle_in_radians = a * pi / 180
    line_length = length
    center_x = x
    center_y = y
    end_x = center_x + line_length * cos(angle_in_radians)
    end_y = center_y + line_length * sin(angle_in_radians)

    canvas.create_line(x,y,end_x,end_y)

    angle_in_radians = a * pi / 180
    line_length = length
    center_x = end_x
    center_y = end_y
    fill_x = center_x + line_length * cos(angle_in_radians)
    fill_y = center_y + line_length * sin(angle_in_radians)

    canvas.create_line(end_x,end_y,fill_x,fill_y,fill="white",width="3")

    angle_in_radians = b * pi / 180
    line_length = length
    center_x = end_x
    center_y = end_y
    end_xx = center_x + line_length * cos(angle_in_radians)
    end_yy = center_y + line_length * sin(angle_in_radians)

    canvas.create_line(end_x,end_y, end_xx,end_yy)

    angle_in_radians = c * pi / 180
    line_length = length
    center_x = end_xx
    center_y = end_yy
    end_xxx = center_x + line_length * cos(angle_in_radians)
    end_yyy = center_y + line_length * sin(angle_in_radians)

    canvas.create_line(end_xx,end_yy, end_xxx,end_yyy)

    angle_in_radians = d * pi / 180
    line_length = length
    center_x = end_xxx
    center_y = end_yyy
    end_xxxx = center_x + line_length * cos(angle_in_radians)
    end_yyyy = center_y + line_length * sin(angle_in_radians)

    canvas.create_line(end_xxx,end_yyy, end_xxxx,end_yyyy)

    lines(depth-1,x,y,length/3,a,b,c,d)

    lines(depth-1,end_x,end_y,length/3,a - 60,b -60,c -60,d -60)

    lines(depth-1,end_xx,end_yy,length/3,a - 300,b -300,c -300,d -300)

    lines(depth-1,end_xxx,end_yyy,length/3,a,b,c,d)

lines(7,0,500,200,0,-60,-300,0)

root.mainloop()
