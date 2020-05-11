import os

pid1 = os.fork()

if pid1 == 0 :
    print "soy el hijo1", pid1
    exit()
#padre
print "padre" , pid1

pid2 = os.fork()

if pid2 == 0 :
    print "soy el hijo2", pid1, pid2
    exit()


print "soy el padre", pid1, pid2
