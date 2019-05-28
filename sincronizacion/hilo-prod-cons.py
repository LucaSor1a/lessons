#!/usr/bin/python3
import threading
import time
import random

list = []
sem1 = threading.Semaphore(20)
sem2 = threading.Semaphore(0)

def prod(cuanto):
    for i in range(cuanto):
        sem1.acquire()
    #    print ("la lista 1 es: ", list)
        time.sleep(random.randrange(0, 10)/100)
        list.append("X")
        print ("agregando elemento: ",list)        
        sem2.release()
    #print ("la lista al final es: ",list)

def cons(cuanto):
    for i in range(cuanto):
        sem2.acquire()
    #    print ("la lista 2 es: ", list)
        time.sleep(random.randrange(0, 10)/100)
        list.pop()
        print ("sacando elemento: ", list)
        sem1.release()
    #print ("esto es: ",list)
        
t1 = threading.Thread(name="h1", target=prod, args=(200,))
t2 = threading.Thread(target=cons, args=(200,))
t1.start()
t2.start()
t1.join()
t2.join()
print ("esto es: ",list)
