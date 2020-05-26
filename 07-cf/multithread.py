import threading
import time

compartida = 5

def thread_function2(name):
    print ("Thread %s: starting", name)
    time.sleep(2)
    global compartida
    compartida = compartida - 1
    print ("termino el hilo y", compartida)

def thread_function(name):
    print ("Thread %s: starting", name)
    y = threading.Thread(target=thread_function2, args=(2,))
    y.start()
    #dos segundos del hilo y 
#    y.join()
    time.sleep(1)
    global compartida
    compartida = compartida + 1 
    print ("termino el hilo x", compartida )


if __name__ == "__main__":
    x = threading.Thread(target=thread_function, args=(1,))
    x.start()
    x.join()
    time.sleep(2)
    print (compartida)
    exit(0)
