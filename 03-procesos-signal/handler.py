import os
import signal

def handler (nroframe):
    print "me llego la senial", nro


signal.signal(signal.SIGINT, signal.SIG_IGN)
signal.signal(signal.SIGUSR1,handler )
signal.signal(signal.SIGUSR2,handler )

#signal.signal(signal.SIGKILL, signal.SIG_IGN)
print os.getpid()
leido = raw_input()

print leido
