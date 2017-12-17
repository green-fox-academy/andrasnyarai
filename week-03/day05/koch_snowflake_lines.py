from tkinter import *
from math import *

root = Tk()

canvas = Canvas(root, width='600', height='600',bg="white")
canvas.pack()

def lines(depth, x0, y0, length, a, b, c, d):
    if depth == 1:
        return

    angle_in_radians = a * pi / 180
    x1 = x0 + length * cos(angle_in_radians)
    y1 = y0 + length * sin(angle_in_radians)

    canvas.create_line(x0, y0, x1, y1)

    angle_in_radians = a * pi / 180
    x_1 = x1 + length * cos(angle_in_radians)
    y_1 = y1 + length * sin(angle_in_radians)

    canvas.create_line(x1, y1, x_1, y_1, fill="white", width="3")

    angle_in_radians = b * pi / 180
    x2 = x1 + length * cos(angle_in_radians)
    y2 = y1 + length * sin(angle_in_radians)

    canvas.create_line(x1, y1, x2, y2)

    angle_in_radians = c * pi / 180
    x3 = x2 + length * cos(angle_in_radians)
    y3 = y2 + length * sin(angle_in_radians)

    canvas.create_line(x2, y2, x3, y3)

    angle_in_radians = d * pi / 180
    x4 = x3 + length * cos(angle_in_radians)
    y4 = y3 + length * sin(angle_in_radians)

    canvas.create_line(x3, y3, x4, y4)

    lines(depth-1, x0, y0, length/3, a, b, c, d)

    lines(depth-1, x1, y1, length/3, a - 60, b -60, c -60, d -60)

    lines(depth-1, x2, y2, length/3, a - 300, b -300, c -300, d -300)

    lines(depth-1, x3, y3, length/3, a, b, c, d)

lines(7, 150, 200, 100, 0, -60, -300, 0)

lines(7, 450, 200, 100, 120, -300, 180, 120)

height = sqrt(300**2 - (150)**2)

lines(7, 300, 200 + height, 100, 240, 180, -60, 240)

root.mainloop()
