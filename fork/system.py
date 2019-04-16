#!/usr/bin/python
import os
print os.getpid()
retorno = os.system("ps -f")

print " el hijo termino = " , retorno
