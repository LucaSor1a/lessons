import random
import threading
import time


condition = threading.Condition()

box = []
print (box)

def producer():
    while True:
        time.sleep(random.randrange(1, 2))
        condition.acquire()
        num = random.randint(1, 10)
        box.append(num)  # Puts an item into box for consumption.
        print (box)
        if len(box) == 5:
            condition.notify()  # Notifies the consumer about the availability.
            time.sleep(4)
        condition.release()

def consumer():
    while True:
        condition.acquire()
        condition.wait()
        print("consume ...")
        for elemento in range(5):
            box.pop()
            print (box)
            time.sleep(4)
        condition.release()

threads = []

""" 'nloops' is the number of times an item will be produced and consumed.  """

for func in [producer, consumer]:
    threads.append(threading.Thread(target=func))
    threads[-1].start()  # Starts the thread.

for thread in threads:
    thread.join()
print("All done.")
