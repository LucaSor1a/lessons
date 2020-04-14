import os
import time

print os.getpid() , os.getppid()

pid = os.fork()

if pid == 0: #hijo
    os.execv("/bin/ps",("/bin/ps","-f"))
    print "termino el hijo"
    print " escriban lo que quieran ... que NUNCA se va a ejecutar !!! "
    print os.getpid() , os.getppid()
    exit(0)

#padre
print "padre esperando que termine el hijo"
#time.sleep(2)
os.wait()
print "padre termino"
