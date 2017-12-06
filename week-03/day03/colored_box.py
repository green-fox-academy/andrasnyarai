from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw a box that has different colored lines on each edge.
line1 = canvas.create_line(75,75,150,75, fill="red")
line2 = canvas.create_line(150,75,150,150, fill="blue")
line3 = canvas.create_line(150,150,75,150, fill="green")
line3 = canvas.create_line(75,150,75,75, fill="yellow")

root.mainloop()
