from PIL import Image as Im

pic = Im.open("../Pictures/Picture_1.jpg")

#Defining a resized picture
out = pic.resize((128,128))

#Rotating the picture
out = out.rotate(45)

#Showing the picture
out.show()
