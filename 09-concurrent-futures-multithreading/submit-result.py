from concurrent import futures
import os
import time

def tarea(seg):
   print ("worker:", os.getpid())
   time.sleep(seg)
   return seg


print ("padre:" , os.getpid())
seg = 3
hilos = futures.ThreadPoolExecutor( max_workers=3)
futuro = hilos.submit(tarea,seg)
seg = 1
futuro2 = hilos.submit(tarea,seg)

print (futuro,futuro2)
resultado = futuro.result()
resultado2 = futuro2.result()
print (futuro, futuro2)
print ("resultado del primer worker:",resultado)
print ("resultado del segundo worker:",resultado2)
