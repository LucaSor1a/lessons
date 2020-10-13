import time
import os
def event_loop(tareas):
    while tareas:
        actual = tareas.pop(0) #saca la primer tarea
        try:
            print ("----")
            next(actual)
            tareas.append(actual)
        except StopIteration:
            pass

def estudio():
    print ("leo")
    yield
    print ("hago resumen")
    print ("hago resumen",os.getpid())
    print ("hago resumen")
    yield
    print ("repaso")
    yield

def subir():
    print ("subiendo ..1 de 3")
    yield
    print ("subiendo ..2 de 3",os.getpid())
    yield
    print ("subiendo ..3 de 3")
    yield

def face():
    print ("veo fotos ")
    print ("veo mas fotos ")
    print ("veo muchas mas fotos ", os.getpid())
    #print ("subo una foto \"pesada\" a face ")
    #time.sleep(5)
    yield from subir()
    yield
    print ("hago un post de lo mucho que estudio")
    print ("chateo")
    print ("chateo")
    yield
    print ("chateo")
    print ("chateo")


event_loop([estudio(),face()])
