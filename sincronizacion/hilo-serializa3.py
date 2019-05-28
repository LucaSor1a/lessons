#!/usr/bin/python3
import threading
import time
saldo = 1000
sem = threading.Lock() ##se inicializa en 1
def transifere(cuanto):
    global saldo
    for i in range(cuanto):
        saldo = saldo + 1
    sem.release() #le avisa al otro hilo que puede seguir
    time.sleep(5) 
    print ("hago mas cosas y finalmtente termino")

def consulta():
    global saldo
    sem.acquire()
    print ("la consulta del saldo es :" , saldo)

sem.acquire()
t1 = threading.Thread(name="h1", target=transifere, args=(40000,))
t2 = threading.Thread(target=consulta )
t1.start()
t2.start()
t1.join()
t2.join()
print ("valor saldo final", saldo)
