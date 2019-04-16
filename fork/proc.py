#! /usr/bin/python

import os
import time
print "hola mundo"
pid = os.fork()
if pid == 0: #hijo
    print "soy el hijo",os.getpid(), os.getppid()
    os._exit(-1) # exit status
else:
    #time.sleep(1)
    print "soy el padre",os.getpid(), os.getppid()
os.waitpid(pid,0)
print "chau, mi hijo termino"
