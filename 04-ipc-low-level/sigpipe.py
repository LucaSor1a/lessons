import os
import time

fd_r, fd_w = os.pipe()
pid = os.fork()

if pid == 0: #hijo
    os.close(fd_w)
    leido = os.read(fd_r, 100)
    print "leido: ", leido
    os.close(fd_r)
    time.sleep(5)
    exit()    
#padre    
os.close(fd_r)
mensaje = raw_input()
os.write(fd_w, mensaje)
time.sleep(1) # me aseguro que el hijo cierre el descriptor ...
os.write(fd_w, mensaje)
os.wait()
