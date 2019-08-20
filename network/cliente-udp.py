#!/usr/bin/python
import socket

desc= socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
servidor=raw_input("server:")
port=raw_input("port:")
#protocolo sin CONEXION
#desc.connect((servidor, int(port)))
desc.sendto("hola server UDP\n",((servidor,int(port))))
leido = desc.recv(2048)
print leido
