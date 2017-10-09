#On raspberian remove the from PIL and ser the tkinter to Tkinter in all reference locations
import os, tkinter, glob
from PIL import Image, ImageTk, ImageFile
from random import randint

def changeImage():

    ImageFile.LOAD_TRUNCATED_IMAGES = True

    #open the config file and get the image folder location and the display time
    file = open('config.cfg', 'r')
    global fileValues
    fileValues = file.read().split(',')
    file.close()

    global tkpi #need global so that the image does not get derefrenced out of function
    try:

        #get random image\
        filename = getfiles()
        image = Image.open(filename)

        #Resize image for an 800x450 screen
        image = image.resize((800,450), Image.NEAREST)

        #Creates a Tkinter compatible photo image
        tkpi = ImageTk.PhotoImage(image)

        #Put image in a label and place it
        label_image = tkinter.Label(root, image=tkpi)
        label_image.place(x=0,y=0,width=image.size[0],height=image.size[1])

        # call this function again in the value set in the config file
        root.after(fileValues[1], changeImage)

    except ValueError:
        print("Error")

#Get the files in the config directory then randomize them and return the single file name
def getfiles():
    filePath =  fileValues[0]
    try:
        allfiles = glob.glob(filePath + "/*.jpg")

        numfiles = len(allfiles)

        arraypos = (randint(0, numfiles-1))
        print(arraypos)
        return allfiles[arraypos]

    except ValueError:
        thefile = getfiles();
        return thefile

#create this global variable so that the image is not derefrenced
tkpi = None

root = tkinter.Tk()
root.geometry('800x450') # Size Width 800, Heigh 480
changeImage()
root.mainloop()
