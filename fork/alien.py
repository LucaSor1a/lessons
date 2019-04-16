#!/usr/bin/python


import os
print os.getpid()
pid = os.fork()
if pid == 0:
    os.execv("/bin/ps", ("/bin/ps","-f"))
    print "por que no sale esto ?"
    print "el pid del hijo es ", pid

hijo, estado = os.wait()

print "termino hijo pid = ", hijo , estado
