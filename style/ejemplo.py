#!/usr/bin/python
""" este modulo es de ejemplo para ver el estilo que devemos darle a nuestro codigo
Pueden correr pylint para verificarlo  # pylint ejemplo.py """
def cuadrado(var):
    ''' funcion que eleva al cuadrado
    retorna el valor   '''
    return var*var

def main(valor):
    """ el programa arranca por aca """
    print cuadrado(valor)

if __name__ == "__main__":
    main(5)

print " hola a todos"
print __name__
