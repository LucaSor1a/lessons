import threading
import time

saldo = 5
barrera = threading.Barrier(4)

def transferencia(monto):
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
    print ("Thread extrae: starting")
    #dos segundos del hilo y 
    global saldo
    saldo = saldo - monto
    #pto encuentro
    barrera.wait()
    print ("saldo final", saldo )
    time.sleep(2)
    print ("hilo extrae sigue trabajando")


def hb(monto):
    print ("Thread hb: starting")
    #dos segundos del hilo y 
    time.sleep(2)
    global saldo
    saldo = saldo - monto
    #pto encuentro
    barrera.wait()
    print ("saldo final", saldo )
    time.sleep(2)
    print ("hilo extrae sigue trabajando")


def otra(monto):
    print ("Thread otra: starting")
    #dos segundos del hilo y 
    time.sleep(2)
    global saldo
    saldo = saldo + monto
    #pto encuentro
    barrera.wait()
    print ("saldo final", saldo )
    time.sleep(2)
    print ("hilo otra sigue trabajando")


if __name__ == "__main__":
    x = threading.Thread(target=transferencia, args=(10000,))
    y = threading.Thread(target=extrae, args=(2000,))
    z = threading.Thread(target=hb, args=(1500,))
    a = threading.Thread(target=otra, args=(500,))
    x.start()
    y.start()
    z.start()
    a.start()
    x.join()
    y.join()
    z.join()
    a.join()
    time.sleep(2)
    print (saldo)
    exit(0)
