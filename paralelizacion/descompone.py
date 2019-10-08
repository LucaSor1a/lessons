#!/usr/bin/python
import multiprocessing

#Defino la funcion en la cual declaro una lista y un bucle para recorrerla e ir multiplicando
def cuadrado(elemento):
    print elemento*elemento,
    return

#Completo el arreglo de mi lista
lista = [1,2,3,4,8,12,4,5]
print lista
for elemento in lista: 
    cuadrado(elemento)

