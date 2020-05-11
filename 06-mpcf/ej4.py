import time
import concurrent.futures
import random

start = time.perf_counter()


def do_nothing(seg):
    print ("espero {} seg".format(seg))
    time.sleep(seg)
    return "ya espere {}".format(seg)

hijos = concurrent.futures.ProcessPoolExecutor()
hn = []
for _ in range(16):
    seg = random.randint(1,9)
    hn.append(hijos.submit(do_nothing,seg))

for f in concurrent.futures.as_completed(hn):
    print (f.result())

finish = time.perf_counter()
tt = round(finish-start,3)
print ("tiempo total = ",tt)
