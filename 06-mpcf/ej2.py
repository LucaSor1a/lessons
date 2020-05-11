import time
import multiprocessing

start = time.perf_counter()


def do_nothing():
    print ("espero 1 seg")
    time.sleep(1)
    print ("ya espere")


p1 = multiprocessing.Process(target=do_nothing)
p2 = multiprocessing.Process(target=do_nothing)
p1.start()
p2.start()
p1.join()
p2.join()
finish = time.perf_counter()
tt = round(finish-start,3)
print ("tiempo total = ",tt)
