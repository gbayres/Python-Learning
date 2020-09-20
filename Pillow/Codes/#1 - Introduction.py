from PIL import Image
import os

os.chdir('../Pictures')
pic = Image.open("Picture_1.jpg")

def show_gray(pic):
    #Shows picture in grayscale
    
    pic1 = Image.open(pic)
    #Color conversions are done using convert()
    pic1 = pic1.convert('L')
    #Show the picture
    pic1.show()

def convert_all(new_format):
    #Convert all images in the folder to another format

    for infile in os.listdir():
        outfile = os.path.splitext(infile)[0]+"."+new_format #Splits name and format
        if outfile != infile:
            try:
                Image.open(infile).save(outfile) #Saves the file
            except IOError:
                print ("Cannot convert ", infile)

def getimlist(path):
    #Get list of images
    return [os.path.join(path,f) \
            for f in \
            os.listdir(path) \
            if f.endswith('.jpg')] #We can have a condition at the end... NICE!

def thumb(pic):
    #Creates a thumbnail
    pic.thumbnail((128,128))
    pic.save('teste.thumbnail','JPEG')
