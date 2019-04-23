#! /usr/bin/python

import os
import time
from signal import *
def funcion (nro,frame):
    print ("recibi la signal", nro, " no voy a terminar de correr")
    print frame

signal(SIGINT,funcion)
print "hola mundo"
print "soy el proceso: ",os.getpid()
#leido = os.read(0,1000)
raw_input()
#os.waitpid(pid,0)
print "chau, mi hijo termino"
