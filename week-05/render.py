from tkinter import * 
from PIL import Image, ImageTk
from structure import *

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

anim = MyLabel(root, 'skeleton_idle.gif')
anim.grid(row=0,sticky=N)

t = Label(root, text="____\n" + box.name
    + "\n <lvl " + str(box.lvl)
    + ">\n\u2665 " + str(box.hp)
    + "/" + str(box.max_hp)
    + "\n\u26E8 " + str(box.dp)
    + "\n\u2694 " + str(box.sp),height=8)

t.grid(row=0,sticky=N,pady=60)

root.update_idletasks()