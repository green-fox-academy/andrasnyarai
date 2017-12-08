from tkinter import *

root = Tk()

size = 600

canvas = Canvas(root, width=size, height=size, bg="gold")
canvas.pack()

def block_draw(x,y,SIZE):
    blocks = canvas.create_rectangle(x,y,x + SIZE,y + SIZE)

def pattern_(xx,yy,SIZE):
    if SIZE < 3:
        return

    unity = 1/3*SIZE

    block_draw(
        unity +xx,
         0 +yy,
          unity )
    block_draw(
        2 * unity +xx,
         unity +yy,
          unity)
    block_draw(
        unity +xx,
         2 * unity +yy,
          unity)
    block_draw(
        0 +xx,
         unity +yy,
          unity)

    pattern_(unity +xx, 0 +yy,unity)
    pattern_(2 * unity +xx,unity +yy, unity)
    pattern_(unity +xx,2 * unity +yy, unity)
    pattern_(0 +xx, unity +yy, unity)


pattern_(0,0,size)




root.mainloop()
