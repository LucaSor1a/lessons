#!/usr/bin/python3
import os
import array
fd = os.open("dog.ppm", os.O_RDONLY)
cabecera = os.read(fd,28)
print (cabecera)
imorig = os.read(fd, 180000)
# PPM header
width = 200
height = 298
maxval = 255
ppm_header = 'P6 200 298 255\n'

# PPM image data (filled with blue)
image = array.array('B', [0, 0, 0] * width * height)

# Fill with red the rectangle with origin at (10, 10) and width x height = 50 x 80 pixels
for x in range(0, 298):
    for y in range(0, 200):
        index = 3 * (x * width + y)
#        image[index] = imorig[index]           # red channel
        image[index + 1] = imorig[index + 1]
#        image[index + 2] = imorig[index + 2]
## Save the PPM image as a binary file
f =  open('dog2.ppm', 'wb')
f.write(bytearray(ppm_header, 'ascii'))
image.tofile(f)
