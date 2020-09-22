import socket
import threading
direcciones = socket.getaddrinfo("localhost",5000, socket.AF_UNSPEC,socket.SOCK_STREAM)

def servicio(direccion):
    s = socket.socket(direccion[0], direccion[1])
    s.bind((direccion[4]))
    s.listen(1)
    while True:
        s2,addr = s.accept()
        print (addr)
        enviado = s2.recv(1024)
        respuesta = enviado.decode().upper()
        s2.send(respuesta.encode())
        print (enviado)
        s2.close()
hilo = []
for direccion in direcciones:
    hilo.append( threading.Thread(target=servicio,args=(direccion,)))
#    threading.Thread(target=servicio, args=(1,))

for i in hilo:
    i.start()
for i in hilo:
    i.join()
