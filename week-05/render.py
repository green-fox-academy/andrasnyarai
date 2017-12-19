from tkinter import * 
import datetime
import os
import image
from itertools import count
from PIL import Image, ImageTk
import random

root = Tk()


grid = [[0,0,0,1,0,1,0,0,0,0],
        [0,0,0,1,0,1,0,1,1,0],
        [0,1,1,1,0,1,0,1,1,0],
        [0,0,0,0,0,1,0,0,0,0],
        [1,1,1,1,0,1,1,1,1,0],
        [0,1,0,1,0,0,0,0,1,0],
        [0,1,0,1,0,1,1,0,1,0],
        [0,0,0,0,0,1,1,0,1,0],
        [0,1,1,1,0,0,0,0,0,0],
        [0,0,0,1,0,0,1,0,0,0]]




class MyLabel(Label):
    def __init__(self, master, filename):
        im = Image.open(filename)
        seq =  []
        try:
            while 1:
                seq.append(im.copy())
                im.seek(len(seq)) # skip to next frame
        except EOFError:
            pass # we're done

        try:
            self.delay = im.info['duration']
        except KeyError:
            self.delay = 100

        first = seq[0].convert('RGBA')
        self.frames = [ImageTk.PhotoImage(first)]

        Label.__init__(self, master, image=self.frames[0])

        temp = seq[0]
        for image in seq[1:]:
            temp.paste(image)
            frame = temp.convert('RGBA')
            self.frames.append(ImageTk.PhotoImage(frame))

        self.idx = 0

        self.cancel = self.after(self.delay, self.play)

    def play(self):
        self.config(image=self.frames[self.idx])
        self.idx += 1
        if self.idx == len(self.frames):
            self.idx = 0
        self.cancel = self.after(self.delay, self.play)        






img = PhotoImage(file='floor.png')
img_wall = PhotoImage(file='wall.png')

hero_u = PhotoImage(file='hero-up.png')
hero_d = PhotoImage(file='hero-down.png')
hero_l = PhotoImage(file='hero-left.png')
hero_r = PhotoImage(file='hero-right.png')

crawler = PhotoImage(file='crawler.png')
eye = PhotoImage(file='eye.png')
blob = PhotoImage(file='blob.png')

wall_critter1 = PhotoImage(file='wall_critter1.png')
img_critter1 = PhotoImage(file='floor_critter1.png')

class Map(object):
    u = random.randint(0,9)

    stabilise_critter = True

    def __init__(self, matrix):
        self.matrix = matrix

    def next_level(self):
        pass

    def draw_matrix(self):
        cell_size = 72
        critter = True
        w = random.randint(0,2)
        for j in range(10):
            for i in range(10):
                if self.matrix[i][j] == 0:
                    canvas.create_image(36 + cell_size * j, 36 + cell_size * i, image=img)
                elif self.matrix[i][j] == 1:
                    if i == Map.u and critter:
                        canvas.create_image(36 + cell_size * j, 36 + cell_size * i, image=wall_critter1)
                        critter = False
                    else:
                        canvas.create_image(36 + cell_size * j, 36 + cell_size * i, image=img_wall)
        for j in range(10):
            for i in range(10):
                if self.matrix[i][j] == 0 and w == 2:
                    canvas.create_image(36 + cell_size * j, 36 + cell_size * i, image=img_critter1)


class Box(object):

    def __init__(self, imageu, imaged, imagel, imager):
        d = random.randint(1,6)
        self.testBoxX = 36
        self.testBoxY = 36
        self.imageu = imageu
        self.imaged = imaged
        self.imagel = imagel
        self.imager = imager
        self.a = 0
        self.b = 0
        self.name = "ragnar"
        self.lvl = 1
        self.max_hp = 20 + 3 * d
        self.hp = 20 + 3 * d
        self.dp = 2 * d
        self.sp = 5 + d


    def draw(self, canvas, picture):
        self.picture = picture
        canvas.create_image(self.testBoxX, self.testBoxY, image=picture)

area = Map(grid)
box = Box(hero_u, hero_d, hero_l, hero_r)

# Create a function that can be called when a key pressing happens


def on_key_press(e):
    if e.keycode == 38:
        area.draw_matrix()
        if grid[box.a - 1][box.b] == 1:
            box.draw(canvas, hero_u)
            obj0.draw(canvas, crawler)
            obj1.draw(canvas, crawler)
            obj2.draw(canvas, crawler)
            objboss.draw(canvas, blob)
            return None
        if box.testBoxY == 36:
            box.draw(canvas, hero_u)
            obj0.draw(canvas, crawler)
            obj1.draw(canvas, crawler)
            obj2.draw(canvas, crawler)
            objboss.draw(canvas, blob)
            return None
        else:
            box.a -= 1
            box.testBoxY = box.testBoxY - 72
            box.draw(canvas, hero_u)
            obj0.draw(canvas, crawler)
            obj1.draw(canvas, crawler)
            obj2.draw(canvas, crawler)
            objboss.draw(canvas, blob)
            obj0.tracking_hero()
            obj1.tracking_hero()
            obj2.tracking_hero()
            objboss.tracking_hero()

    elif e.keycode == 40:
        area.draw_matrix()
        if box.testBoxY == 684:
            box.draw(canvas, hero_d)
            obj0.draw(canvas, crawler)
            obj1.draw(canvas, crawler)
            obj2.draw(canvas, crawler)
            objboss.draw(canvas, blob)
            return None
        if grid[box.a + 1][box.b] == 1:
            box.draw(canvas, hero_r)
            obj0.draw(canvas, crawler)
            obj1.draw(canvas, crawler)
            obj2.draw(canvas, crawler)
            objboss.draw(canvas, blob)
            return None
        else:
            box.a += 1
            box.testBoxY = box.testBoxY + 72
            box.draw(canvas, hero_d)
            obj0.draw(canvas, crawler)
            obj1.draw(canvas, crawler)
            obj2.draw(canvas, crawler)
            objboss.draw(canvas, blob)
            obj0.tracking_hero()
            obj1.tracking_hero()
            obj2.tracking_hero()
            objboss.tracking_hero()

    elif e.keycode == 37:
        area.draw_matrix()
        if grid[box.a][box.b - 1] == 1:
            box.draw(canvas, hero_l)
            obj0.draw(canvas, crawler)
            obj1.draw(canvas, crawler)
            obj2.draw(canvas, crawler)
            objboss.draw(canvas, blob)
            return None
        if box.testBoxX == 36:
            box.draw(canvas, hero_l)
            obj0.draw(canvas, crawler)
            obj1.draw(canvas, crawler)
            obj2.draw(canvas, crawler)
            objboss.draw(canvas, blob)
            return None
        else:
            box.b -= 1
            box.testBoxX = box.testBoxX - 72
            box.draw(canvas, hero_l)
            obj0.draw(canvas, crawler)
            obj1.draw(canvas, crawler)
            obj2.draw(canvas, crawler)
            objboss.draw(canvas, blob)
            obj0.tracking_hero()
            obj1.tracking_hero()
            obj2.tracking_hero()
            objboss.tracking_hero()

    elif e.keycode == 39:
        area.draw_matrix()
        if box.testBoxX == 684:
            box.draw(canvas, hero_r)
            obj0.draw(canvas, crawler)
            obj1.draw(canvas, crawler)
            obj2.draw(canvas, crawler)
            objboss.draw(canvas, blob)
            return None
        if grid[box.a][box.b + 1] == 1:
            box.draw(canvas, hero_r)
            obj0.draw(canvas, crawler)
            obj1.draw(canvas, crawler)
            obj2.draw(canvas, crawler)
            objboss.draw(canvas, blob)
            return None
        else:
            box.b += 1
            box.testBoxX = box.testBoxX + 72
            box.draw(canvas, hero_r)
            obj0.draw(canvas, crawler)
            obj1.draw(canvas, crawler)
            obj2.draw(canvas, crawler)
            objboss.draw(canvas, blob)
            obj0.tracking_hero()
            obj1.tracking_hero()
            obj2.tracking_hero()
            objboss.tracking_hero()
                
positions = []

class Enemy(object):
    x = 1

    def __init__(self):
        d = random.randint(1,6)
        self.testBoxX = 36
        self.testBoxY = 36
        self.lvl = Enemy.x
        self.hp = 2 * Enemy.x * d
        self.dp = Enemy.x/2 * d
        self.sp = Enemy.x * d

    def get_enemy_location(self):
        enemy_random_location = True
        while enemy_random_location:
            z = random.randint(0,9)
            x = random.randint(1,9)
            if grid[z][x] == 0 and [z,x] not in positions:
                enemy_random_location = False
                positions.append([z,x])
                return [z,x]

    def changing_to_coordinates(self):
        coordinates = self.get_enemy_location()
        self.testBoxY += (coordinates[0])*72
        self.testBoxX += (coordinates[1])*72
        return str(coordinates[0]) + str(coordinates[1])

    def tracking_hero(self):
        if box.testBoxX == self.testBoxX and box.testBoxY == self.testBoxY:
            print('kacsa')

    def draw(self, canvas, picture):
        self.picture = picture
        canvas.create_image(self.testBoxX, self.testBoxY, image=picture)

class Boss(Enemy):

    def __init__(self):
        d = random.randint(1,6)
        self.testBoxX = 36
        self.testBoxY = 36
        self.lvl = Enemy.x
        self.hp = 2 * Enemy.x * d + d
        self.dp = Enemy.x/2 * d + d/2
        self.sp = Enemy.x * d + Enemy.x

obj0 = Enemy()
obj1 = Enemy()
obj2 = Enemy()
objboss = Boss()

obj0.changing_to_coordinates()
obj1.changing_to_coordinates()
obj2.changing_to_coordinates()
objboss.changing_to_coordinates()


canvas = Canvas(root, width=720, height=720)
anim = MyLabel(root, 'skeleton_idle.gif')
anim.grid(row=0,sticky=N)

T = Label(root, text="____\n" + box.name + "\n <lvl " + str(box.lvl) + ">\n\u2665 " + str(box.max_hp) + "/" + str(box.hp) + "\n\u26E8 " + str(box.dp) + "\n\u2694 " + str(box.sp),height=7)
T.grid(row=0,sticky=N,pady=60)

# Tell the canvas that we prepared a function that can deal with the key press events
canvas.bind("<KeyPress>", on_key_press)
canvas.grid(row=0, column=1, rowspan=4)
# Select the canvas to be in focused so it actually recieves the key hittings
canvas.focus_set()
# Draw the box in the initial position
area.draw_matrix()
box.draw(canvas, hero_d)
obj0.draw(canvas, crawler)
obj1.draw(canvas, crawler)
obj2.draw(canvas, crawler)
objboss.draw(canvas, blob)
#time
root.mainloop()