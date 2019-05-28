#!/usr/bin/python3
import threading
import time
saldo = 1000
encuentro = threading.Barrier(4)
def transf1(cuanto):
    global saldo
    saldo = saldo + cuanto
    ##encuentro
    encuentro.wait()
    print ("el saldo final de tansf1 es :" , saldo)
    time.sleep(4) 
    print ("hago mas cosas en transf1")

def transf2(cuanto):
    global saldo
    saldo = saldo + cuanto
    ##encuentro
    encuentro.wait()
    print ("el saldo final de tansf2 es :" , saldo)
    time.sleep(2) 
    print ("hago mas cosas en transf2 " )

def extrae1(cuanto):
    global saldo
    saldo = saldo - cuanto
    ##encuentro
    encuentro.wait()
    print ("el saldo final de extrae es :" , saldo)
    time.sleep(3) 
    print ("hago mas cosas en extrae " )

def extrae2(cuanto):
    global saldo
    saldo = saldo - cuanto
    ##encuentro
    encuentro.wait()
    print ("el saldo final de extrae2 es :" , saldo)
    time.sleep(3) 
    print ("hago mas cosas en extrae2 " )
hilos=[]
hilos.append(threading.Thread(target=transf1, args=(40000,)))
hilos.append(threading.Thread(target=transf2, args=(500,) ))
hilos.append(threading.Thread(target=extrae1, args=(15000,) ))
hilos.append(threading.Thread(target=extrae2, args=(2300,) ))

for hilo in hilos:
    hilo.start()

for hilo in hilos:
    hilo.join()

print ("valor saldo final", saldo)
