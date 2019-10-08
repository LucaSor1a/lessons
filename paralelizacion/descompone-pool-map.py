#!/usr/bin/python
import multiprocessing as mp
import os

#Defino la funcion en la cual declaro una lista y un bucle para recorrerla e ir multiplicando
def cuadrado(elemento):
    #print "subindice", subindice, "valor" ,elemento * elemento
    print (os.getpid(), elemento*elemento) 
    #print (elemento*elemento)
    return

#Completo el arreglo de mi lista
lista = [1,2,3,4,8,12,4,5]
#p = []
#nro_hijos = len (lista)
#pul = mp.Pool(mp.cpu_count())
pool = mp.Pool(4) #crea 4 hijos trabajadores
pool.map(cuadrado, lista)
print ("terminaron los 4 hijos")
