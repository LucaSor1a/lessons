import os
import time

print os.getpid() , os.getppid()

pid = os.fork()

if pid == 0: #hijo
    print ("hijo" , os.getpid() , os.getppid())
    time.sleep(20)
    print ("hijo" , os.getpid() , os.getppid())
    exit(0)

#padre
#time.sleep(2)
#os.wait()
print "padre termino"
