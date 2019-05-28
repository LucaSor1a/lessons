#!/usr/bin/python3
import threading
import time
saldo = 1000
def transifere(cuanto):
    global saldo
    for i in range(cuanto):
        saldo = saldo + 1
    time.sleep(5) 
    print ("hago mas cosas y finalmtente termino")

def consulta():
    global saldo
    print ("la consulta del saldo es :" , saldo)

t1 = threading.Thread(name="h1", target=transifere, args=(40000,))
t2 = threading.Thread(target=consulta )
t1.start()
t2.start()
t1.join()
t2.join()
print ("valor saldo final", saldo)
