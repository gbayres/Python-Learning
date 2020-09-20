from PIL import Image

#Opening a picture
photo = Image.open("../Pictures/Picture_1.png")

#We will define a crop box
#It will follow this format:
#(x0, y0, x0 + length , y0 + height)
box = (200,200,400,300)

#Here we will crop a region of the picture
region = photo.crop(box)

#Rotate it, using any of the following
#region = region.transpose(Image.ROTATE_180)
region = region.rotate(180)

#Paste it on the photo
photo.paste(region,box)

#Show it
photo.show()

