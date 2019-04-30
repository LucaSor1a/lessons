#!/usr/bin/python
import os
import time
import multiprocessing

def func1():
    leido = mq.get()
    print "hijo1" , leido, os.getpid(),os.getppid()

def func2():
    leido = mq.get()
    print "hijo2" , leido, os.getpid(),os.getppid()

print "soy el padre"

h1 = multiprocessing.Process(target=func1,  args=())
h2 = multiprocessing.Process(target=func2,  args=())
mq = multiprocessing.Queue()
h1.start()
h2.start()

time.sleep(3)
mq.put ("despertate")
mq.put ("despertate")

h2.join()
h1.join()

print "terminaron los hijos"
