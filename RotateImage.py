# Simple enough, just import everything from tkinter.
from tkinter import *
import time

# download and install pillow:
# http://www.lfd.uci.edu/~gohlke/pythonlibs/#pillow
from PIL import Image, ImageTk

import glob
from array import array
from random import randint
import threading



# Here, we are creating our class, Window, and inheriting from the Frame
# class. Frame is a class from the tkinter module. (see Lib/tkinter/__init__)
class Window(Frame):
    # Define settings upon initialization. Here you can specify
    def __init__(self, master=None):
        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)


        # reference to the master widget, which is the tk window
        self.master = master

        # with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    # Creation of init_window
    def init_window(self):
        # changing the title of our master widget
        self.master.title("GUI")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.client_exit)

        # added "file" to our menu
        menu.add_cascade(label="File", menu=file)

        # create the file object)
        edit = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Show Img", command=self.showImg)
        edit.add_command(label="Show Text", command=self.showText)

        # added "file" to our menu
        menu.add_cascade(label="Edit", menu=edit)


    def startImage(self):

        print("running")

    def showImg(self):
        #threading.Timer(5, Window.showImg).join(1)
        #time.sleep(10)
        try:
            filename = self.getfiles()
            load = Image.open(filename)
            widths = self.winfo_width()
            heights = self.winfo_height()
            widths = widths - 10
            heights = heights - 10

            try:
                load = load.resize((widths,heights), Image.NEAREST)
            except ValueError:
                print("Error")

            render = ImageTk.PhotoImage(load)
            # labels can be text or images
            img = Label(self, image=render)

            img.image = render
            img.place(x=0, y=0)
        except ValueError:
            print("Start Over")

    def showText(self):
        text = Label(self, text="Hey there good lookin!")
        text.pack()

    def client_exit(self):
        exit()

    def getfiles(self):
        print("Getting file")
        try:
            allfiles = glob.glob("/Users/hoarec/Documents/Pictures/*.jpg")

            numfiles = len(allfiles)

            arraypos = (randint(0, numfiles))
            print(arraypos)
            return allfiles[arraypos]
            # print(glob.glob("/User/hoarec/Documents/Pictures/*.jpg"))
            # return  #glob.glob("/Users/hoarec/Documents/Pictures/*.jpg")
        except ValueError:
            print("Error Get File")
            #thefile = root.getfiles();
            #return thefile

    def _resize_image(self, event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


# root window created. Here, that would be the only window, but
# you can later have windows within windows.
root = Tk()
root.attributes('-fullscreen',True)
root.wm_overrideredirect(True)
#root.wm_attributes('-type', 'splash')
root.overrideredirect(0)


#root.geometry("800x600")

# creation of an instance
app = Window(root)





# mainloop

root.mainloop()