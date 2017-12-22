import random
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
canvas = Canvas(root, width=720, height=720)

hero_u = PhotoImage(file='hero-up.png')
hero_d = PhotoImage(file='hero-down.png')
hero_l = PhotoImage(file='hero-left.png')
hero_r = PhotoImage(file='hero-right.png')
hero_u_k = PhotoImage(file='hero_up_k.png')
hero_d_k = PhotoImage(file='hero_down_k.png')
hero_l_k = PhotoImage(file='hero_left_k.png')
hero_r_k = PhotoImage(file='hero_right_k.png')

img = PhotoImage(file='floor.png')
img_wall = PhotoImage(file='wall.png')
wall_critter1 = PhotoImage(file='wall_critter1.png')
crawler = PhotoImage(file='crawler.png')
blob = PhotoImage(file='blob.png')

jungle = PhotoImage(file='jungle_floor.png')
jungle_wall = PhotoImage(file='jungle_wall.png')
jungle_wall_c = PhotoImage(file='jungle_wall_c.png')
eye = PhotoImage(file='eye.png')
summoner = PhotoImage(file="summoner.png")

desert = PhotoImage(file='floor_desert.png')
desert_wall = PhotoImage(file='wall_desert.png')
desert_wall_c = PhotoImage(file='wall_desert_critter.png')
axeman = PhotoImage(file="axeman.png")
goblin = PhotoImage(file='goblin.png')

tesseract_floor = PhotoImage(file='tesseract_floor.png')
tesseract_wall = PhotoImage(file='tesseract_wall.png')
tesseract_wall_c = PhotoImage(file='tesseract_wall_c.png')
knight = PhotoImage(file='knight.png')
wizard = PhotoImage(file='wizard.png')

maze_floor = PhotoImage(file='maze_floor.png')
maze_wall = PhotoImage(file='maze_wall.png')
maze_wall_c = PhotoImage(file='maze_wall_c.png')
cubix = PhotoImage(file='cubix.png')
koch = PhotoImage(file='koch.png')

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

class Map(object):

    def __init__(self, matrix):
        self.matrix = matrix

        self.floor = img
        self.wall = img_wall
        self.wall_critter = wall_critter1
        self.creep = crawler
        self.boss = blob

        self.assets = 1

        self.area = 1
        self.random_generate = 3

    def load_next_level(self):
        k = random.randint(0, 10)
        if k == 10:
            box.hp = box.max_hp
        if 6 <= k <= 9:
            box.hp += (box.max_hp - box.hp) // 3
        if k <= 5:
            box.hp += (box.max_hp - box.hp) // 10
        box.have_key = False
        army.occupied = []
        army.positions = []
        army.lvl = []
        box.testBoxX = 36
        box.testBoxY = 36
        box.a = 0
        box.b = 0
        self.assets += 1
        self.area += 1
        self.random_generate += 1
        if self.assets == 1:
            self.floor = img
            self.wall = img_wall
            self.wall_critter = wall_critter1
            self.creep = crawler
            self.boss = blob
        if self.assets == 2:
            self.floor = desert
            self.wall = desert_wall
            self.wall_critter = desert_wall_c
            self.creep = axeman
            self.boss = goblin
        if self.assets == 3:
            self.floor = jungle
            self.wall = jungle_wall
            self.wall_critter = jungle_wall_c
            self.creep = eye
            self.boss = summoner
        if self.assets == 4:
            self.floor = tesseract_floor
            self.wall = tesseract_wall
            self.wall_critter = tesseract_wall_c
            self.creep = knight
            self.boss = wizard
        if self.assets == 5:
            self.floor = maze_floor
            self.wall = maze_wall
            self.wall_critter = maze_wall_c
            self.creep = cubix
            self.boss = koch
            self.assets = 0
        army.spawn(area.random_generate, area.area)
        area.draw_matrix()
        try:
            army.draw_item()
        except IndexError:
            pass
        box.draw(canvas)

    def draw_matrix(self):
        u = random.randint(0,9)
        cell_size = 72
        critter = True
        for j in range(10):
            for i in range(10):
                if self.matrix[i][j] == 0:
                    canvas.create_image(36 + cell_size * j, 36 + cell_size * i, image=self.floor)
                elif self.matrix[i][j] == 1:
                    if i == u and critter:
                        canvas.create_image(36 + cell_size * j, 36 + cell_size * i, image=self.wall_critter)
                        critter = False
                    else:
                        canvas.create_image(36 + cell_size * j, 36 + cell_size * i, image=self.wall)

area = Map(grid)

class Box(object):

    def __init__(self):
        d = random.randint(1,6)
        self.testBoxX = 36
        self.testBoxY = 36
        self.image = hero_d
        self.imageup = hero_u
        self.imagedown = hero_d
        self.imageleft = hero_l
        self.imageright = hero_r
        self.imagestrikeup = hero_u_k
        self.imagestrikedown = hero_d_k
        self.imagestrikeleft = hero_l_k
        self.imagestrikeright = hero_r_k
        self.a = 0
        self.b = 0
        self.name = "ragnar"
        self.lvl = 1
        self.max_hp = 20 + 3 * d
        self.hp = 20 + 3 * d
        self.dp = 2 * d
        self.sp = 5 + d
        self.have_key = False
        self.boss_dead = False

    def level_up(self):
        d = random.randint(1,6)
        self.lvl += 1
        self.max_hp += d
        self.dp += d
        self.sp += d

    def move(self, x_px, y_px):
        canvas.move(self.picture, x_px, y_px)

    def draw(self, canvas):
        self.picture = canvas.create_image(self.testBoxX, self.testBoxY, image=self.image)

    def kill_and_load(self, __who__):
        if army.lvl[__who__].type == 'creep':
            if army.lvl[__who__].have_key == True:
                self.have_key = True
        elif army.lvl[__who__].type == 'boss':
                self.boss_dead = True
        army.lvl[__who__].dead()
        del(army.occupied[__who__])
        del(army.lvl[__who__])
        del(army.positions[__who__])
        if self.have_key and self.boss_dead:
            area.load_next_level()

    def attack(self, attr):
        if attr is 'U':
            index = army.occupied.index([self.testBoxX, self.testBoxY - 72])
            self.battle(army.lvl[index])
            canvas.itemconfigure(box.picture, image = box.imagestrikeup)
            self.kill_and_load(index)


        if attr is 'R':
            index = army.occupied.index([self.testBoxX + 72, self.testBoxY])
            self.battle(army.lvl[index])
            canvas.itemconfigure(box.picture, image = box.imagestrikeright)
            self.kill_and_load(index)


        if attr is 'D':
            index = army.occupied.index([self.testBoxX, self.testBoxY + 72])
            self.battle(army.lvl[index])
            canvas.itemconfigure(box.picture, image = box.imagestrikedown)
            self.kill_and_load(index)

        if attr is 'L':
            index = army.occupied.index([self.testBoxX - 72, self.testBoxY])
            self.battle(army.lvl[index])
            canvas.itemconfigure(box.picture, image = box.imagestrikeleft)
            self.kill_and_load(index)

    def battle(self, actual_enemy):
        fight = True
        while fight:
            strike = True
            d = random.randint(1,6)
            if 2*d + self.sp > actual_enemy.dp and strike:
                actual_enemy.hp -= 2*d + self.sp - actual_enemy.dp
                strike = False
            if 2*d + actual_enemy.sp > self.dp and not strike:
                self.hp -= 2*d + actual_enemy.sp - self.dp
                strike = True
            if self.hp < 0:
                fight = False
                # hero die
            if actual_enemy.hp < 0:
                fight = False
                if d > 3:
                    self.level_up()
    
    def hover(self):
        if [self.a, self.b] in army.positions:
            self.hp -= 5

box = Box()

class Enemy(object):
    
    def __init__(self):
        d = random.randint(1,6)
        self.testBoxX = 36
        self.testBoxY = 36
        self.type = 'creep'
        self.lvl = 1
        self.hp = 2 * 1 * d
        self.dp = 1 * d
        self.sp = 1 * d + 1
        self.a = 0
        self.b = 0
        self.changing_to_coordinates()
        self.have_key = False
        self.main_image = area.creep
        self.directions = []
        self.valid = []
        
    def get_enemy_location(self):
        enemy_random_location = True
        while enemy_random_location:
            z = random.randint(0,9)
            x = random.randint(1,9)
            if grid[z][x] == 0 and [z,x] not in army.positions:
                enemy_random_location = False
                return [z,x]

    def changing_to_coordinates(self):
        coordinates = self.get_enemy_location()
        army.positions.append(coordinates)
        self.testBoxY += (coordinates[0])*72
        self.testBoxX += (coordinates[1])*72
        self.a = coordinates[0]
        self.b = coordinates[1]
        # print(coordinates[0])
        # print(coordinates[1])
        # return [self.testBoxX, self.testBoxY]

    def draw(self, canvas):
        self.image = canvas.create_image(self.testBoxX, self.testBoxY, image=self.main_image)

    def dead(self):
        canvas.lower(self.image)

    def move(self):

        print(army.positions)
        movements = []

        up = self.move_up()
        down = self.move_down()
        left = self.move_left()
        right = self.move_right()

        if up:
            movements.append('U')
        if down:
            movements.append('D')
        if left:
            movements.append('L')
        if right:
            movements.append('R')

        if len(movements) == 0:
            return
        else:
            t = random.randint(0,len(movements)-1)
            # print(t)
            destination = movements[t]
            if destination == 'U':
                canvas.move(self.image, 0, -72)
                self.testBoxY = self.testBoxY - 72
                self.a -= 1
            if destination == 'D':
                canvas.move(self.image, 0, + 72)
                self.testBoxY = self.testBoxY + 72
                self.a += 1
            if destination == 'L':
                canvas.move(self.image, -72 , 0)
                self.b -= 1
                self.testBoxX = self.testBoxX - 72
            if destination == 'R':
                canvas.move(self.image, +72, 0)
                self.b += 1
                self.testBoxX = self.testBoxX + 72

    def move_up(self):
        if self.a == 0:
            return 
        if [self.a - 1,self.b] in army.positions:
            return
        if grid[self.a - 1][self.b] == 1:
            return
        else:
            return True

    def move_down(self):
        if self.a == 9:
            return
        if [self.a + 1,self.b] in army.positions:
            return
        if grid[self.a + 1][self.b] == 1:
            return
        else:
            return True

    def move_left(self):
        if self.b == 0:
            return
        if [self.a,self.b - 1] in army.positions:
            return
        if grid[self.a][self.b - 1] == 1:
            return
        else:
            return True

    def move_right(self):
        if self.b == 9:
            return
        if [self.a,self.b + 1] in army.positions:
            return
        if grid[self.a][self.b + 1] == 1:
            return
        else:
            return True

    def set_levels(self, amount):
        d = random.randint(1,6)
        if self.type == 'boss':
            self.lvl = amount
            self.hp = 2 * amount * d + d + 1
            self.dp = amount * d + d
            self.sp = amount * d + amount
        if self.type == 'creep':
            self.lvl = amount
            self.hp = 2 * amount * d
            self.dp = amount * d
            self.sp = amount * d

class Boss(Enemy):

    def __init__(self):
        super().__init__()
        d = random.randint(1,6)
        self.testBoxX = 36
        self.testBoxY = 36
        self.type = 'boss'
        self.lvl = 1
        self.hp = 0
        self.dp = 0
        self.sp = 0
        self.changing_to_coordinates()
        self.main_image = area.boss
        box.boss_dead = False
        
class Monsters(object):

    def __init__(self):
        self.lvl = []
        self.occupied = []
        self.positions = []

    def spawn(self, how_many_monsters, lvl_of):
        t = random.randint(0,10)
        if t == 10:
            lvl_of == lvl_of + 2
        if 6 <= t <= 9:
            lvl_of == lvl_of + 1
        if t <= 5:
            lvl_of == lvl_of
        boss = Boss()
        boss.set_levels(lvl_of)
        boss.get_enemy_location()
        self.occupied.append([boss.testBoxX,boss.testBoxY])
        self.lvl.append(boss)
        u = random.randint(1, how_many_monsters)
        for i in range(0, how_many_monsters):
            enemy = Enemy()
            enemy.set_levels(lvl_of)
            enemy.get_enemy_location()

            self.occupied.append([enemy.testBoxX,enemy.testBoxY])
            self.lvl.append(enemy)
        self.lvl[-u].have_key = True

    def mass_move(self):
        for _which_ in range(len(self.lvl)):
            del(self.occupied[0])
            del(self.positions[0])
            self.lvl[_which_].move()
            self.positions.append([self.lvl[_which_].a, self.lvl[_which_].b])
            self.occupied.append([self.lvl[_which_].testBoxX, self.lvl[_which_].testBoxY])

    def draw_item(self):
        for i in range(len(army.lvl)):
            self.lvl[i].draw(canvas)

army = Monsters()
