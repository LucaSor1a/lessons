import asyncio
import time

def estudiar():
    print ("leyendo")
    print (time.localtime()[3:6])

def cpu_bound():
    cont = 0
    for i in range(10000):
        for j in range (10000):
            cont = cont + j

loop = asyncio.get_event_loop()

loop.call_later(3,estudiar)
loop.call_soon(cpu_bound)
#ejecuta todo lo registado
print (time.localtime()[3:6])
loop.run_forever()

