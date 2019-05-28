#!/usr/bin/python3
import threading
saldo = 1000
mutex = threading.Lock()
def depo(cuanto):
    global saldo
    for i in range(cuanto):
        mutex.acquire()
        saldo = saldo + 1
        mutex.release()
#    print ("termino el hilo depo saldo:" , saldo)

def extra(cuanto):
    global saldo
    for i in range(cuanto):
        mutex.acquire()
        saldo = saldo - 1
        mutex.release()
#    print ("termino el hilo extra saldo:" , saldo)

t1 = threading.Thread(name="h1", target=depo, args=(10000,))
t2 = threading.Thread(target=extra, args=(10000,))
t1.start()
t2.start()
t1.join()
t2.join()
print ("valor saldo final", saldo)
