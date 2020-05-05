import time
import multiprocessing

start = time.perf_counter()


def do_nothing():
    print ("espero 1 seg")
    time.sleep(1)
    print ("ya espere")


p = multiprocessing.Process(target=do_nothing)
p.start()
p.join()
finish = time.perf_counter()
tt = round(finish-start,3)
print ("tiempo total = ",tt)
