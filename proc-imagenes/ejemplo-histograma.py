#!/usr/bin/python3
#histograma de ocurrencia de nros de 1 digito
arreglo = [1,3,2,5,7,5,4,7,8,4,3,2,7,0,7,2,4,6,7]
hn=[0]*10
for nro in arreglo:
    hn[nro] = hn[nro] + 1
print (hn)
#histograma de largo de palabras (maximo 11)
cadena = "esto es una prueba para que los estudiantes comprendan los histogramas"
hp=[0]*11
for palabra in cadena.split():
    hp[len(palabra)-1] = hp[len(palabra)-1] + 1 #no hay palabras de largo 0  ;-)
print (hp)
