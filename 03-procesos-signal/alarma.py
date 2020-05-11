import os
import time
import signal

def handler (nro,frame):
    signal.alarm(3)
    print "llego alarma ", nro
    time.sleep(1)


signal.signal(signal.SIGALRM,handler )

print os.getpid()
signal.alarm(3)
leido = raw_input()

print leido
