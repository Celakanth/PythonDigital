from tkinter import *
from PIL import Image, ImageTk
import glob
from array import array
from random import randint
import threading


def __init__(self, master):
    Frame.__init__(self, master)
    print("Starting")
    root.rollimage()

def resize(event):
    size = (event.width, event.height)
    resized = root.original.resize(size,Image.ANTIALIAS)
    root.image = ImageTk.PhotoImage(resized)
    root.display.delete("IMG")
    root.display.create_image(0, 0, image=root.image, anchor=NW, tags="IMG")

def getfiles():
    print("Getting file")
    try:
        allfiles = glob.glob("/Users/hoarec/Documents/Pictures/*.jpg")

        numfiles = len(allfiles)

        arraypos = (randint(0, numfiles))
        print(arraypos)
        return allfiles[arraypos]
        #print(glob.glob("/User/hoarec/Documents/Pictures/*.jpg"))
        #return  #glob.glob("/Users/hoarec/Documents/Pictures/*.jpg")
    except ValueError:
        print("Error Get File")
        thefile = root.getfiles();
        return thefile

def rollimage():
    t = threading.Timer(5.0, root.rollimage())
    t.start()

    try:
        filename = root.getfiles()
        print(filename)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        root.original = Image.open(filename)
        root.image = ImageTk.PhotoImage(root.original)
        root.display = Canvas(root, bd=0, highlightthickness=0)
        root.display.create_image(0, 0, image=root.image, anchor=NW, tags="IMG")
        root.display.grid(row=0, sticky=W + E + N + S)
        root.pack(fill=BOTH, expand=1)
        root.bind("<Configure>", root.resize)
    except ValueError:
        print("Error")

def setNexr():
    print("Next Image")
    try:
        filename = root.getfiles()
        print(filename)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        root.original = Image.open(filename)
        root.image = ImageTk.PhotoImage(root.original)
        root.display = Canvas(root, bd=0, highlightthickness=0)
        root.display.create_image(0, 0, image=root.image, anchor=NW, tags="IMG")
        root.display.grid(row=0, sticky=W + E + N + S)
        root.pack(fill=BOTH, expand=1)
        root.bind("<Configure>", root.resize)
    except ValueError:
        print("Error")


root = Tk()
root.attributes('-fullscreen', True)
app = rollimage();
app.mainloop()
