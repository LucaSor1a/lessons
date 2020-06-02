import threading
import time

saldo = 5
candado = threading.Lock()

def transferencia(monto):
    print ("Thread transf: starting")
    global saldo
    for i in range(monto):
        candado.acquire()
        saldo = saldo + 1
        candado.release()
    print ("termino el hilo transferencia", saldo)

def extrae(monto):
    print ("Thread extrae: starting")
    #dos segundos del hilo y 
    global saldo
    for i in range(monto):
        candado.acquire()
        saldo = saldo - 1
        candado.release()
    print ("termino el hilo extraccion", saldo )


if __name__ == "__main__":
    x = threading.Thread(target=transferencia, args=(100000,))
    y = threading.Thread(target=extrae, args=(100000,))
    x.start()
    y.start()
    x.join()
    y.join()
    print (saldo)
    exit(0)
