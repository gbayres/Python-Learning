from PIL import Image
import os

os.chdir('../Pictures')

pic1 = Image.open('Picture_1.jpg')

#Color conversoins are done using convert()

pic1 = pic1.convert('L')

#Show the picture

pic1.show()

