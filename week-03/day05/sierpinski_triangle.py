from tkinter import *

root = Tk()

size = 600

canvas = Canvas(root, width=size, height=size, bg="#f0fff0")
canvas.pack()

def drawSierpinski(depth,x0, y0, x1, y1, x2, y2):
    if (depth <= 0):
        canvas.create_polygon(x0, y0, x1, y1, x2, y2, fill="#ff69b4", outline="#3a3a3a", width="0.5")
    else:
        drawSierpinski(depth-1,x0,y0,average(x0,x1), average(y0,y1),average(x0,x2), average(y0,y2))
        drawSierpinski(depth-1,average(x0,x1), average(y0,y1),x1, y1,average(x1,x2), average(y1, y2))
        drawSierpinski(depth-1,average(x0,x2), average(y0,y2),average(x1,x2), average(y1, y2),x2, y2)

def average(u,v):
    return (u+v)/2

drawSierpinski(5,300,50,0,500,600,500)

root.mainloop()
