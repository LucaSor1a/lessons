#!/usr/bin/python3

import threading
import time

def fun1():
    time.sleep(1)
    nombre = threading.currentThread().getName()
    print ("termino el hilo",nombre)

def fun2():
    time.sleep(3)
    nombre = threading.currentThread().getName()
    print ("termino el hilo",nombre)

ini = time.time()
t1 = threading.Thread(name="h1", target=fun1)
t2 = threading.Thread(target=fun2)
t1.start()
t2.start()
t1.join()
t2.join()
#fun1()
#fun2()
fin = time.time()
print ("tiempo total", fin - ini)
