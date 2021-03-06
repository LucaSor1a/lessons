import threading
import time

saldo = 5
sem = threading.Lock()

def transferencia(monto):
    print ("Thread transf: starting")
    time.sleep(5)
    global saldo
    saldo = saldo + monto
    sem.release()
    print ("termino el hilo transferencia", saldo)

def extrae(monto):
    print ("Thread extrae: starting")
    #dos segundos del hilo y 
    global saldo
    sem.acquire()
    saldo = saldo - monto
    print ("termino el hilo extraccion", saldo )


if __name__ == "__main__":
    sem.acquire()
    x = threading.Thread(target=transferencia, args=(10000,))
    y = threading.Thread(target=extrae, args=(2000,))
    x.start()
    y.start()
    x.join()
    y.join()
    time.sleep(2)
    print (saldo)
    exit(0)
