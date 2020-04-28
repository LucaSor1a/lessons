from multiprocessing import Process
import os
import time

def info(title):
    print(title)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())
#    time.sleep(2)

def f(name):
    info('function f')
    print('hello', name)

if __name__ == '__main__':
    info('funcion main')
    p = Process(target=f, args=('bob',))
    p.start()
    p.join(1)
    p.terminate()
    print(p.pid)
    print (p.is_alive())
    print (p.exitcode)
