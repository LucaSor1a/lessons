#!/usr/bin/python3
import threading
import time
saldo = 1000
done_1_2 = threading.Semaphore(0)
done_1_e = threading.Semaphore(0)
done_2_1 = threading.Semaphore(0)
done_2_e = threading.Semaphore(0)
done_e_1 = threading.Semaphore(0)
done_e_2 = threading.Semaphore(0)
def transf1(cuanto):
    global saldo
    saldo = saldo + cuanto
    done_1_2.release()
    done_1_e.release()
    done_2_1.acquire()
    done_e_1.acquire()
    ##encuentro
    print ("el saldo final de tansf1 es :" , saldo)
    time.sleep(4) 
    print ("hago mas cosas en transf1")

def transf2(cuanto):
    global saldo
    saldo = saldo + cuanto
    done_2_1.release()
    done_2_e.release()
    done_1_2.acquire()
    done_e_2.acquire()
    ##encuentro
    print ("el saldo final de tansf2 es :" , saldo)
    time.sleep(2) 
    print ("hago mas cosas en transf2 " )

def extrae(cuanto):
    global saldo
    saldo = saldo - cuanto
    done_e_1.release()
    done_e_2.release()
    done_1_e.acquire()
    done_2_e.acquire()
    ##encuentro
    print ("el saldo final de extrae es :" , saldo)
    time.sleep(3) 
    print ("hago mas cosas en extrae " )
hilos=[]
hilos.append(threading.Thread(target=transf1, args=(40000,)))
hilos.append(threading.Thread(target=transf2, args=(500,) ))
hilos.append(threading.Thread(target=extrae, args=(15000,) ))

for hilo in hilos:
    hilo.start()

for hilo in hilos:
    hilo.join()

print ("valor saldo final", saldo)
