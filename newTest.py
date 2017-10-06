from tkinter import *

from PIL import Image, ImageTk

import threading
import glob
from array import array
from random import randint


root = Tk()
root.title("Title")
root.geometry("600x600")
root.configure(background="black")


class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)


    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)

    def getfiles(self):
        try:
            allfiles = glob.glob("/Users/hoarec/Documents/Pictures/*.jpg")

            numfiles = len(allfiles)

            arraypos = (randint(0, numfiles))
            print(arraypos)
            return allfiles[arraypos]
            # print(glob.glob("/User/hoarec/Documents/Pictures/*.jpg"))
            # return  #glob.glob("/Users/hoarec/Documents/Pictures/*.jpg")
        except ValueError:
            thefile = self.getfiles();
            return thefile

    def setimage(self):
        filename = self.getfiles()

        self.image = Image.open(filename)
        self.img_copy = self.image.copy()

        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)
        e.pack(fill=BOTH, expand=YES)


e = Example(root)
def process():
    t = threading.Timer(5.0, e.setimage)
    t.start()
process()
e.mainloop()