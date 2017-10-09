import os, Tkinter, glob
import Image, ImageTk, ImageFile
from random import randint


def changeImage():

    ImageFile.LOAD_TRUNCATED_IMAGES = True

    global tkpi #need global so that the image does not get derefrenced out of function
    try:
        #gets list of file names in certain directory. In this case, the directory it is in
        dirlist = glob.glob("/Users/hoarec/Documents/Pictures/*.jpg")

        #get random image\
        widths = root.winfo_width()
        heights = root.winfo_height()
        widths = widths - 10
        heights = heights - 10

        #randInt = random.randint(0, (len(dirlist) - 1))
        filename = getfiles()
        image = Image.open(filename)
        image = image.resize((800,450), Image.NEAREST)

        #set size to show, in this case the whole picture
       # root.geometry('%dx%d' % (image.size[0],image.size[1]))

        #Creates a Tkinter compatible photo image
        tkpi = ImageTk.PhotoImage(image)

        #Put image in a label and place it
        label_image = Tkinter.Label(root, image=tkpi)
        label_image.place(x=0,y=0,width=image.size[0],height=image.size[1])

        # call this function again in 1/2 a second
        root.after(10000, changeImage)
    except ValueError:
        print("Error")


def getfiles():
    try:
        allfiles = glob.glob("/home/pi/Pictures/*.jpg")

        numfiles = len(allfiles)

        arraypos = (randint(0, numfiles-1))
        print(arraypos)
        return allfiles[arraypos]
        # print(glob.glob("/User/hoarec/Documents/Pictures/*.jpg"))
        # return  #glob.glob("/Users/hoarec/Documents/Pictures/*.jpg")
    except ValueError:
        thefile = getfiles();
        return thefile

tkpi = None #create this global variable so that the image is not derefrenced

root = Tkinter.Tk()
#root.geometry(width=500,height=500)
#root.geometry('+%d+%d' % (-5,-5)) #controls where the window is
#root.attributes('-alpha', 0.0) #For icon
#root.iconify()
#root = tkinter.Toplevel(root)
#root.attributes('-fullscreen',True)
root.geometry('800x450') # Size 200, 200
changeImage()
root.mainloop()
