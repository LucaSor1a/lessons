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
hr=[0]*256
hg=[0]*256
hb=[0]*256
ht=[0]*256
# PPM image data (filled with blue)

# Fill with red the rectangle with origin at (10, 10) and width x height = 50 x 80 pixels
for x in range(0, height):
    for y in range(0,width):
        index = 3 * (x * width + y)
        hr[imorig[index]] = hr[imorig[index]] + 1
        ht[imorig[index]] = ht[imorig[index]] + 1
        hg[imorig[index + 1]] = hg[imorig[index + 1]] + 1
        ht[imorig[index + 1]] = ht[imorig[index + 1]] + 1
        hb[imorig[index + 2]] = hb[imorig[index + 2]] + 1
        ht[imorig[index + 2]] = ht[imorig[index + 2]] + 1

#print (hr)
import matplotlib.pyplot as plt
plt.plot(hr)
plt.plot(hg)
plt.plot(hb)
plt.plot(ht)
plt.show()
