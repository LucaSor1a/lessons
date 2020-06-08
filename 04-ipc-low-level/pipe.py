import os
import time

fd_r,fd_w = os.pipe()
pid = os.fork()

if pid == 0: #hijo
    os.close(fd_w)
    time.sleep(5)
    while True:
        leido = os.read(fd_r, 100)
        print "leido: ", leido
        if leido == '':
            break
    exit()    
#padre    
os.close(fd_r)
mensaje = raw_input()
os.write(fd_w, mensaje)
time.sleep(7)
os.close(fd_w)
os.wait()
