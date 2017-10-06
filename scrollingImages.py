import os, tkinter,  random, glob
from PIL import Image, ImageTk, ImageFile


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

        randInt = random.randint(0, (len(dirlist) - 1))
        image = Image.open(dirlist[randInt])
        image = image.resize((widths,heights), Image.NEAREST)

        #set size to show, in this case the whole picture
        #root.geometry('%dx%d' % (image.size[0],image.size[1]))

        #Creates a Tkinter compatible photo image
        tkpi = ImageTk.PhotoImage(image)

        #Put image in a label and place it
        label_image = tkinter.Label(root, image=tkpi)
        label_image.place(x=0,y=0,width=image.size[0],height=image.size[1])

        # call this function again in 1/2 a second
        root.after(10000, changeImage)
    except ValueError:
        print("Error")


tkpi = None #create this global variable so that the image is not derefrenced

root = tkinter.Tk()
#root.geometry('+%d+%d' % (-5,-5)) #controls where the window is
#root.attributes('-alpha', 0.0) #For icon
root.iconify()
root = tkinter.Toplevel(root)
root.attributes('-fullscreen',True)
changeImage()
root.mainloop()