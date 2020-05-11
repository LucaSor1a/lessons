import time
import multiprocessing
import random

start = time.perf_counter()


def do_nothing(seg):
    print ("espero {} seg".format(seg))
    time.sleep(seg)
    print ("ya espere")
proc = []
for i in range(10):
    seg = random.randint(1,10)
    proc.append( multiprocessing.Process(target=do_nothing,args = (seg,) ))
    proc[i].start()


print ( proc )

for i in range(10):
    proc[i].join()

finish = time.perf_counter()
tt = round(finish-start,3)
print ("tiempo total = ",tt)
