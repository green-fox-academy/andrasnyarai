from render import *

def happenings():
    
    t = Label(root, text="____\n" + box.name
     + "\n <lvl " + str(box.lvl)
      + ">\n\u2665 " + str(box.hp)
       + "/" + str(box.max_hp)
        + "\n\u26E8 " + str(box.dp)
         + "\n\u2694 " + str(box.sp),height=7)

    t.grid(row=0,sticky=N,pady=95)

    if box.have_key:
        n = Label(root, text='\u26B7')
        n.grid(row=0,sticky=N,pady=195)
    if not box.have_key:
        m = Label(root, text='     ')
        m.grid(row=0,sticky=N,pady=195)

    root.update_idletasks()

    army.mass_move()
    box.hover()
    box.death()

    root.after(1000, happenings)

def on_key_press(e):

    if e.keycode == 38:
        if area.matrix[box.a - 1][box.b] == 1:
            canvas.itemconfigure(box.picture, image = box.imageup)
            return None
        if box.testBoxY == 36:
            canvas.itemconfigure(box.picture, image = box.imageup)
            return None
        else:
            canvas.itemconfigure(box.picture, image = box.imageup)
            box.move(0, - 72)
            box.testBoxY = box.testBoxY - 72
            box.a -= 1
            box.hover()

    elif e.keycode == 40:
        if box.testBoxY == 684:
            canvas.itemconfigure(box.picture, image = box.imagedown)
            return None
        if area.matrix[box.a + 1][box.b] == 1:
            canvas.itemconfigure(box.picture, image = box.imagedown)
            return None
        else:
            canvas.itemconfigure(box.picture, image = box.imagedown)
            box.move(0, + 72)
            box.testBoxY = box.testBoxY + 72
            box.a += 1
            box.hover()

    elif e.keycode == 37:
        if area.matrix[box.a][box.b - 1] == 1:
            canvas.itemconfigure(box.picture, image = box.imageleft)
            return None
        if box.testBoxX == 36:
            canvas.itemconfigure(box.picture, image = box.imageleft)
            return None
        else:
            canvas.itemconfigure(box.picture, image = box.imageleft)
            box.move(-72 , 0)
            box.b -= 1
            box.testBoxX = box.testBoxX - 72
            box.hover()

    elif e.keycode == 39:
        if box.testBoxX == 684:
            canvas.itemconfigure(box.picture, image = box.imageright)
            return None
        if area.matrix[box.a][box.b + 1] == 1:
            canvas.itemconfigure(box.picture, image = box.imageright)
            return None
        else:
            canvas.itemconfigure(box.picture, image = box.imageright)
            box.move( +72, 0)
            box.b += 1
            box.testBoxX = box.testBoxX + 72
            box.hover()

    elif e.keycode == 32:
        if [box.testBoxX, box.testBoxY - 72] in army.occupied:   
            box.attack('U')
        else:
            pass
            if [box.testBoxX + 72, box.testBoxY] in army.occupied: 
                box.attack('R')
            else:
                pass
                if [box.testBoxX, box.testBoxY + 72] in army.occupied:
                    box.attack('D')
                else:
                    pass
                    if [box.testBoxX - 72, box.testBoxY] in army.occupied:
                        box.attack('L')


root.update_idletasks()

canvas.bind("<KeyPress>", on_key_press)
canvas.focus_set()
canvas.grid(row=0, column=1, rowspan=4, pady=25)

root.after(1000, happenings)
root.mainloop()