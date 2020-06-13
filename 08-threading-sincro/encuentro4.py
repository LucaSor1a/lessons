import threading
import time

saldo = 5
barrera = threading.Barrier(3)

def transferencia(monto):
    while (True):
        print ("Thread transf: starting")
        global saldo
    #    time.sleep(5)
        saldo = saldo + monto
        #pto encuentro
        barrera.wait()
        print ("saldo final", saldo)
        time.sleep(1)
        print ("hilo transf sigue trabajando")

def extrae(monto):
    while (True):
        print ("Thread extrae: starting")
        #dos segundos del hilo y 
        global saldo
        saldo = saldo - monto
        #pto encuentro
        barrera.wait()
        print ("saldo final", saldo )
        time.sleep(2)
        print ("hilo extrae sigue trabajando")


if __name__ == "__main__":
    x = threading.Thread(target=transferencia, args=(10000,))
    y = threading.Thread(target=extrae, args=(2000,))
    x.start()
    y.start()
    while (True):
        barrera.wait()
        print ("saldo final", saldo )
        barrera = threading.Barrier(3)
    x.join()
    y.join()
    time.sleep(2)
    print (saldo)
    exit(0)
