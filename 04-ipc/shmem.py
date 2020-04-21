import mmap
import os
import time
import signal

def lee(nro, frame):
    leido = area.read(10)
    print leido

signal.signal(signal.SIGUSR1, lee)
area = mmap.mmap(-1, 100)

pid = os.fork()

if pid == 0: #hijo
    area.write("algo")
    time.sleep(1)
    os.kill(os.getppid(), signal.SIGUSR1)
    exit()

#padre
os.wait()
