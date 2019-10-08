#!/usr/bin/python
import multiprocessing as mp
import os

#Defino la funcion en la cual declaro una lista y un bucle para recorrerla e ir multiplicando
def cuadrado(subindice,elemento):
    #print "subindice", subindice, "valor" ,elemento * elemento
    #print (os.getpid(), subindice, elemento*elemento) 
    return (subindice,elemento*elemento)

def call (retorno):
    global lista2
    lista2.append(retorno)

#Completo el arreglo de mi lista
lista = [1,2,3,4,8,12,4,5]
lista2 = []
#nro_hijos = len (lista)
#pul = mp.Pool(mp.cpu_count())
pool = mp.Pool(4) #crea 4 hijos trabajadores
sub = 0
for elemento in lista:
    pool.apply_async(cuadrado, args=(sub,elemento,), callback=call)
    sub = sub + 1
pool.close()
pool.join()
print ("terminaron los 4 hijos")
print (lista)
print (lista2)
