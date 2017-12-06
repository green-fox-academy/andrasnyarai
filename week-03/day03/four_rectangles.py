from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw four different size and color rectangles.

rect4 = canvas.create_rectangle(75,75,225,225,fill="green")
rect3 = canvas.create_rectangle(50,50,175,175,fill="yellow")
rect2 = canvas.create_rectangle(25,25,125,125,fill="blue")
rect1 = canvas.create_rectangle(0,0,75,75,fill="red")

root.mainloop()
