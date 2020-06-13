from concurrent import futures
import os
import time

def tarea(seg):
   print ("worker:", os.getpid())
   time.sleep(seg)
   return seg


print ("padre:" , os.getpid())
seg = 3
hilos = futures.ThreadPoolExecutor(max_workers=45)
#hilos = futures.ThreadPoolExecutor()
retornos_futuros = [ hilos.submit(tarea,i)  for i in range(45,0,-1)]
print (retornos_futuros)
for r in futures.as_completed(retornos_futuros):
    print (r.result())

