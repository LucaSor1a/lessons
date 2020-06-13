from concurrent import futures
import os
import time
import threading

saldo = 1000
candado = threading.Lock()

def suma(monto):
   global saldo
   print ("worker:", os.getpid())
   for i in range(monto):
        candado.acquire()
        saldo = saldo + 1
        candado.release()
   return saldo

def resta(monto):
   global saldo
   print ("worker:", os.getpid())
   for i in range(monto):
        candado.acquire()
        saldo = saldo - 1
        candado.release()
   return saldo

print ("hilo main:" , os.getpid())
seg = 3
hilos = futures.ThreadPoolExecutor(max_workers=4)
#hilos = futures.ThreadPoolExecutor()
retornos_futuros = [ hilos.submit(suma,i)  for i in (100000 , 100000,100000)]
retornos_futuro2 = [ hilos.submit(resta,i)  for i in (100000 , 100000,100000)]
for i in range(len(retornos_futuro2)):
    retornos_futuros.append(retornos_futuro2[i])
for r in futures.as_completed(retornos_futuros):
    print (r.result())
print (saldo)

