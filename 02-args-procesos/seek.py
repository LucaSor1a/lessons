import os
fd = os.open("servi.txt", os.O_RDWR)
leido = os.read(fd,10)
print leido
os.lseek(fd,20,2)
os.write(fd, "donde escribo??")

