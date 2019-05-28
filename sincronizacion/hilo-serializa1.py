#!/usr/bin/python3
import threading
saldo = 1000
def transifere(cuanto):
    global saldo
    for i in range(cuanto):
        saldo = saldo + 1
#    print ("termino el hilo depo saldo:" , saldo)

def consulta():
    global saldo
    print ("la consulta del saldo es :" , saldo)

t1 = threading.Thread(name="h1", target=transifere, args=(40000,))
t2 = threading.Thread(target=consulta )
t1.start()
t1.join()
t2.start()
t2.join()
print ("valor saldo final", saldo)
