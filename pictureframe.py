from tkinter import *
from PIL import Image, ImageTk
import glob
from array import array
from random import randint
import threading



class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        t = threading.Timer(5.0, self.rollimage())
        t.start()



    def resize(self, event):
        size = (event.width, event.height)
        resized = self.original.resize(size,Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized)
        self.display.delete("IMG")
        self.display.create_image(0, 0, image=self.image, anchor=NW, tags="IMG")

    def getfiles(self):
        try:
            allfiles = glob.glob("/Users/hoarec/Documents/Pictures/*.jpg")

            numfiles = len(allfiles)

            arraypos = (randint(0, numfiles))
            print(arraypos)
            return allfiles[arraypos]
            #print(glob.glob("/User/hoarec/Documents/Pictures/*.jpg"))
            #return  #glob.glob("/Users/hoarec/Documents/Pictures/*.jpg")
        except ValueError:
            thefile = self.getfiles();
            return thefile

    def rollimage(self):
        while (True):
            try:
                filename = self.getfiles()
                print(filename)
                self.columnconfigure(0, weight=1)
                self.rowconfigure(0, weight=1)
                self.original = Image.open(filename)
                self.image = ImageTk.PhotoImage(self.original)
                self.display = Canvas(self, bd=0, highlightthickness=0)
                self.display.create_image(0, 0, image=self.image, anchor=NW, tags="IMG")
                self.display.grid(row=0, sticky=W + E + N + S)
                self.pack(fill=BOTH, expand=1)
                self.bind("<Configure>", self.resize)
            except ValueError:
                print("Error")


root = Tk()
root.attributes('-fullscreen', True)
app = App(root)

#app.mainloop()
#root.destroy()

