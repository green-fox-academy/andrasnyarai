from tkinter import *
import random
root = Tk()

canvas = Canvas(root ,bg="black", width='300', height='300')
canvas.pack()

# draw the night sky:
# - The background should be black
# - The stars should be small squares
# - The stars should have random positions on the canvas
# - The stars should have random color (some shade of grey)

def styling_box(size,color):
    x1 = random.randrange(0,290)
    x2 = random.randrange(0,290)
    y1 = x1 + 10
    y2 = x2 + 10
    center_box = canvas.create_rectangle(x1,x2,y1,y2,fill=color)


for i in range(0, 300, 15):
    grey = random.randrange(0,255)
    colorval = "#%02x%02x%02x" % (grey, grey, grey)
    styling_box(i,colorval)


root.mainloop()
