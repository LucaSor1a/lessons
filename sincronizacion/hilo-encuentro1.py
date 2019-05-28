#!/usr/bin/python3
import threading
import time
saldo = 1000
espero_a_1 = threading.Semaphore(0)
espero_a_2 = threading.Semaphore(0)
def transifere1(cuanto):
    global saldo
    saldo = saldo + cuanto
    espero_a_1.release()
    espero_a_2.acquire()
    ##encuentro
    print ("el saldo final de tasnfiere1 es :" , saldo)
    time.sleep(5) 
    print ("hago mas cosas y finalmtente termino")

def transfiere2(cuanto):
    global saldo
    saldo = saldo + cuanto
    espero_a_2.release()
    espero_a_1.acquire()
    ##encuentro
    print ("el saldo final de tasnfiere2 es :" , saldo)
    time.sleep(2) 
    print ("hago mas cosas en transfiere2 " )

t1 = threading.Thread(name="h1", target=transifere1, args=(40000,))
t2 = threading.Thread(target=transfiere2, args=(500,) )
t1.start()
t2.start()
t1.join()
t2.join()
print ("valor saldo final", saldo)
