#Here wi will learn to intereact with the map

from PIL import Image
from pylab import array, imshow, ginput, show

im = array(Image.open('../Pictures/Picture_1.jpg'))
imshow(im)

print ("Please click 3 points")

x = ginput(3)

print ("You clicked:", x)

show()
