from concurrent import futures
import os
import time

def tarea(seg):
   print ("worker:", os.getpid()," espero:", seg)
   time.sleep(seg)
   return seg


print ("padre:" , os.getpid())
seg = 3
hilos = futures.ThreadPoolExecutor(max_workers=3)
resultado_a_futuro = hilos.map(tarea ,range(4,0,-1))
print (list(resultado_a_futuro))
