#!/usr/bin/python
import multiprocessing
import os
resultado = []
mq = multiprocessing.Queue()

#Defino la funcion en la cual declaro una lista y un bucle para recorrerla e ir multiplicando
def cuadrado(elemento,subindice):
    #print "subindice", subindice, "valor" ,elemento * elemento
    #print os.getpid()
    mq.put([subindice,elemento*elemento])
    return

#Completo el arreglo de mi lista
lista = [1,2,3,4,8,12,4,5]
p = []
nro_hijos = len (lista)
for i in range(nro_hijos):
    p.append( multiprocessing.Process(target=cuadrado, args=(lista[i],i)))
    p[i].start()
#espero que terminen todos los procesos antes de leer 
#no es necesario si uso el mq.get()
#for i in range(nro_hijos):
#    p[i].join()

lista2 = []
for i in range(nro_hijos):
    lista2.append(0)
for i in range(nro_hijos):
    #si no hay mensajes de los hijos (porque todavia no terminaron) los espera
    a = mq.get()
    lista2[a[0]] = a[1] 
print lista
print "terminaron todos los hijos, eleva al cuadrado"
print lista2
