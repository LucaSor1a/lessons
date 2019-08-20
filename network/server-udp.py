#!/usr/bin/python
import socket

desc= socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
servidor=raw_input("mi ip:")
port=raw_input("mi port:")
desc.bind((servidor, int(port)))
#Protocolo sin conexion
#desc.listen(20)
#newdesc,cli = desc.accept()
while True:
    leido,cli = desc.recvfrom(1024)
    print cli
    print leido
    desc.sendto("saludos cliente\n", cli)
