from tkinter import * 
from structure import *
from PIL import Image, ImageTk

class MyLabel(Label):
    def __init__(self, master, filename):
        im = Image.open(filename)
        seq =  []
        try:
            while 1:
                seq.append(im.copy())
                im.seek(len(seq))
        except EOFError:
            pass

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

anim = MyLabel(root, 'assets/skeleton_idle.gif')
anim.grid(row=0,sticky=N, pady=25)

t = Label(root, text="____\n" + box.name
    + "\n <lvl " + str(box.lvl)
    + ">\n\u2665 " + str(box.hp)
    + "/" + str(box.max_hp)
    + "\n\u26E8 " + str(box.dp)
    + "\n\u2694 " + str(box.sp),height=7)

t.grid(row=0,sticky=N,pady=95)

def close_window(): 
    root.destroy()

ex_button = Button(root, relief=GROOVE, text = "e x i t", command = close_window)
ex_button.grid(row=0, column=3, sticky=N, padx=10, pady=25)

frame = Frame(root,bg="black", width=720, height=720)
frame.grid(row=0, column=1, rowspan=4, pady=25)

def start_the_game(): 
    army.spawn(area.random_generate,area.area)
    area.draw_matrix()
    box.draw(canvas)
    army.draw_item()
    frame.destroy()

start_button = Button(frame, relief=GROOVE, text = "S T A R T", command = start_the_game)
start_button.grid()
