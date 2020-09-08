import socket
import os
import signal


# no quiero zombiessss
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# otra vez .... address already in use 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("127.0.0.1",5000))
s.listen(1)
while True:
    s2,addr = s.accept()
    pid = os.fork()
    if pid == 0:
        print (addr)
        enviado = s2.recv(1024)
        respuesta = enviado.decode().upper()
        s2.send(respuesta.encode())
        print (enviado)
        s2.close()
        exit()
    # descriptores abiertos ...
    s2.close()
