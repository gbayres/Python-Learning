from PIL import Image as Im
from pylab import array, figure, gray, contour, axis, show, hist

#Read image to array
im = array(Im.open("../Pictures/Picture_1.jpg").convert("L"))

#Create a new figure
figure()

#Remove colors
gray()

#Show contours with origin upper left corner
contour(im, origin="image")
axis('equal')
axis('off')

figure()
hist(im.flatten(),128)

show()
