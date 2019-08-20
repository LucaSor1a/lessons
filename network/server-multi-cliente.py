#!/usr/bin/python
import socket

desc= socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
#servidor=raw_input("mi ip:")
#port=raw_input("mi port:")
desc.bind(("192.168.14.250", 5000))
desc.listen(20)
while True:
    newdesc,cli = desc.accept()
    print cli
    leido = newdesc.recv(2048)
    print leido
    newdesc.send("saludos cliente\n")
    newdesc.close()
