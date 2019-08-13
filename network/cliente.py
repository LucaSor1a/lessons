#!/usr/bin/python
import socket

desc= socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
servidor=raw_input("server:")
port=raw_input("port:")
desc.connect((servidor, int(port)))
consulta=raw_input("consulta:")
desc.send(consulta+"\n")
leido = desc.recv(2048)
print leido,
while leido != '':
    leido = desc.recv(2048)
    print leido,
