#!/usr/bin/python3

import threading
import time

def Fun1():
    """hace algun procesamiento que demora 1 seg"""
    time.sleep(1)
    print ("termino la fun1")

def Fun2():
    """hace algun procesamiento que demora 2 seg"""
    time.sleep(3)
    print ("termino la fun2")
Ini = time.time()
Fun1()
Fun2()
Fin = time.time()
print ("tiempo total", Fin - Ini)
