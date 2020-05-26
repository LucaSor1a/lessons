import os
var = "quien soy?"
pid1 = os.fork()

if pid1 == 0 :
    print "soy el hijo1", pid1
    var = var + " hijo1"
    print var
    exit()
#padre
print "padre" , pid1

var = var + " padre"
print var

pid2 = os.fork()

if pid2 == 0 :
    print "soy el hijo2", pid1, pid2
    var = var + " hijo2"
    print var
    exit()


print "soy el padre", pid1, pid2
print var
