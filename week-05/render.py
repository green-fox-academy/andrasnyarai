from tkinter import * 
import datetime
root = Tk()
canvas = Canvas(root, width=720, height=720)
canvas.pack()

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


img = PhotoImage(file='floor.png')
img_wall = PhotoImage(file='wall.png')

hero_u = PhotoImage(file='hero-up.png')
hero_d = PhotoImage(file='hero-down.png')
hero_l = PhotoImage(file='hero-left.png')
hero_r = PhotoImage(file='hero-right.png')

class Map(object):

    def __init__(self, matrix):
        self.matrix = matrix

    def draw_matrix(self):
        cell_size = 72
        for j in range(10):
            for i in range(10):
                if self.matrix[i][j] == 0:
                    canvas.create_image(36 + cell_size * j, 36 + cell_size * i, image=img)
                elif self.matrix[i][j] == 1:
                    canvas.create_image(36 + cell_size * j, 36 + cell_size * i, image=img_wall)

class Box(object):
    def __init__(self, imageu, imaged, imagel, imager):
        self.testBoxX = 36
        self.testBoxY = 36
        self.imageu = imageu
        self.imaged = imaged
        self.imagel = imagel
        self.imager = imager
        self.a = 0
        self.b = 0


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
            return None
        if box.testBoxY == 36:
            box.draw(canvas, hero_u)
            return None
        else:
            box.a -= 1
            print(grid[box.a][box.b])
            box.testBoxY = box.testBoxY - 72
            box.draw(canvas, hero_u)
    elif e.keycode == 40:
        area.draw_matrix()
        try:
            if grid[box.a + 1][box.b] == 1:
                box.draw(canvas, hero_r)
                return None
        except IndexError:
            box.draw(canvas, hero_d)
            return None
        if box.testBoxY == 684:
            box.draw(canvas, hero_d)
            return None
        else:
            box.a += 1
            print(grid[box.a][box.b])
            box.testBoxY = box.testBoxY + 72
            box.draw(canvas, hero_d)
    elif e.keycode == 37:
        area.draw_matrix()
        if grid[box.a][box.b - 1] == 1:
            box.draw(canvas, hero_l)
            return None
        if box.testBoxX == 36:
            box.draw(canvas, hero_l)
            return None
        else:
            box.b -= 1
            print(grid[box.a][box.b])
            box.testBoxX = box.testBoxX - 72
            box.draw(canvas, hero_l)
    elif e.keycode == 39:
        area.draw_matrix()
        try:
            if grid[box.a][box.b + 1] == 1:
                box.draw(canvas, hero_r)
                return None
        except IndexError:
            box.draw(canvas, hero_r)
            return None
        if box.testBoxX == 684:
            box.draw(canvas, hero_r)
            return None
        else:
            box.b += 1
            print(grid[box.a][box.b])
            box.testBoxX = box.testBoxX + 72
            box.draw(canvas, hero_r)
    
    # and lower if the key that was pressed the down arrow
    # draw the box again in the new position

# Tell the canvas that we prepared a function that can deal with the key press events
canvas.bind("<KeyPress>", on_key_press)
canvas.pack()

# Select the canvas to be in focused so it actually recieves the key hittings
canvas.focus_set()

# Draw the box in the initial position
area.draw_matrix()
box.draw(canvas, hero_d)

#time

root.mainloop()