from concurrent import futures
import os
import time

def tarea(seg):
   print ("worker:", os.getpid()) 
   time.sleep(seg)
   return seg


print ("padre:" , os.getpid()) 
seg = 3
hijo = futures.ProcessPoolExecutor( max_workers=3)
futuro = hijo.submit(tarea,seg)
seg = 1
futuro2 = hijo.submit(tarea,seg)

print (futuro)
resultado = futuro.result()
resultado2 = futuro2.result()
print (futuro)
print ("resultado del primer worker:",resultado)
print ("resultado del segundo worker:",resultado2)
