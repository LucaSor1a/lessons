from concurrent import futures
import os
import time

def tarea(seg):
   print ("worker:", os.getpid()) 
   time.sleep(seg)
   return seg


print ("padre:" , os.getpid()) 
seg = 3
hijo = futures.ProcessPoolExecutor(max_workers=3)
espera = [ hijo.submit(tarea,i)  for i in range(4,0,-1)]

for r in futures.as_completed(espera):
    print (r.result())

