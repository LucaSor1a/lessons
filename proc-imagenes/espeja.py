#!/usr/bin/python3
import array
import os
fd = os.open("dog.ppm", os.O_RDONLY)
cabecera = os.read(fd,28)
imorig = os.read(fd, 180000)
# PPM header
width = 200
height = 298
maxval = 255
image = array.array('B', [0, 0, 0] * width * height)

for y in range(0, height):
    for x in range(0, width):
        index = 3 * (x + (width * y))
        escalon = 3*(width*(y + 1) - (x+1)) # funcion escalon para expejar horizontalmente 
        #print (index, escalon)
        image[escalon]  = imorig[index]          # red channel
        image[escalon + 1] = imorig[index + 1]   # green channel
        image[escalon + 2] = imorig[index + 2]   # blue channel
## Save the PPM image as a binary file
f =  open('dog2.ppm', 'wb')
f.write(bytearray(cabecera.decode(), 'ascii'))
image.tofile(f)
