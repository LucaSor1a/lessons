from concurrent import futures
import os
import time

def tarea(seg):
   print ("worker:", os.getpid()," espero:", seg) 
   time.sleep(seg)
   return seg


print ("padre:" , os.getpid()) 
seg = 3
hijos = futures.ProcessPoolExecutor(max_workers=3)
resultado = hijos.map(tarea ,range(4,0,-1))

print (list(resultado))
