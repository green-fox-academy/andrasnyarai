from tkinter import *
from math import *
import random

root = Tk()
canvas = Canvas(root, width=600, height=600)
canvas.pack()

class Walker(object):

    def __init__(self):
        self.depth = 0
        self.area = []
        self.positions = []
        self.jump_points = []
        self.start_x = 300
        self.start_y = 300
        self.fill_up_perimeter()
        print(self.area)

    def start(self):
        self.positions.append([self.start_x,self.start_y])

    def empty(self):
        self.positions = []
        self.jump_points = []

    def fill_up_perimeter(self):
        for num in range(0, 620, 20):
            self.area.append([num, 0])
            self.area.append([num, 600])
            self.area.append([0, num])
            self.area.append([600, num])

    def random_walk(self, depth, x, y, length):
        if depth == 0:
            return

        A = False
        B = False
        C = False
        D = False

        active = True
        while active:

            a = random.choice([0, 180, 90, -90])

            angle_in_radians = a * pi / 180
            x1 = int(x) + length * cos(angle_in_radians)
            y1 = int(y) + length * sin(angle_in_radians)
            x1 = int(x1)
            y1 = int(y1)

            if a == 0 and [x1,y1] in self.positions or int(round(x1)) == 600:
                A = True
            if a == 180 and [x1,y1] in self.positions or int(round(x1)) == 0:
                B = True
            if a == 90 and [x1,y1] in self.positions or int(round(y1)) == 600:
                C = True
            if a == -90 and [x1,y1] in self.positions or int(round(y1)) == 0:
                D = True

            while A and B and C and D:
                self.jump_points = [c for c in self.jump_points if c != [x,y]]
                if len(w.jump_points) == 0:
                    return
                # d = random.randint(0,len(w.jump_points) - 1)
                x = int(w.jump_points[-1][0])
                y = int(w.jump_points[-1][1])
                x = int(x)
                y = int(y)

                a = random.choice([0, 180, 90, -90])

                angle_in_radians = a * pi / 180
                x1 = int(x) + length * cos(angle_in_radians)
                y1 = int(y) + length * sin(angle_in_radians)

                A = False
                B = False
                C = False
                D = False

                print('jump')
                print(depth)
                
            if [x1,y1] not in self.positions:

                if 0 < int(x1) < 600 and 0 < int(y1) < 600:

                    self.positions.append([int(x1),int(y1)])

                    self.jump_points.append([int(x1),int(y1)])
                    color_rgb = "#%02x%02x%02x" % (depth//2, 255, 255)
                    canvas.create_line(int(x), int(y), int(x1), int(y1), fill=color_rgb, width=5)
                    active = False

        print(y1)

        self.random_walk(depth - 1, x1, y1, length)

w = Walker()

def on_key_press(e):

    if e.keysym == "Return":
        w.depth += 10
        print(w.depth)

    elif e.keysym == "space":
        canvas.create_rectangle(0, 0, 600, 600, fill="black", outline="black")
        w.start()
        w.random_walk(w.depth, w.start_x, w.start_y, 30)
        w.empty()
        print(w.depth)
        print('____________________________________')

    elif e.keysym == "minus":
        w.depth -= 1
        print(w.depth)

root.update_idletasks()

canvas.bind("<KeyPress>", on_key_press)
canvas.focus_set()

root.mainloop()
