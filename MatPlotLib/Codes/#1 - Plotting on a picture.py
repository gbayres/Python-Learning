from PIL import Image as Im
from pylab import * #array, imshow, plot, title, show

#Open image as array
im = array(Im.open("../Pictures/Picture_1.jpg"))

#Plot the image
imshow(im)

#Some points
x = [100,100,400,400]
y = [200,500,200,500]

#Plot with red star markers
plot(x,y,'r.') 

#Plot a line connecting the first two points
plot(x[2:4], y[2:4], 'r--')

#Draws an arrow
#arrow(300,300,300,300)

#Add a title and show the plot
title("Plotting the picture") 
show()
