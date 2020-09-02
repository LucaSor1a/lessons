import concurrent.futures
import socket
import os

def servicio(s2, addr):
    print (addr)
    enviado = s2.recv(1024)
    respuesta = enviado.decode().upper()
    s2.send(respuesta.encode())
    print (enviado)
    s2.close()

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1",5000))
        s.listen(2)
        while True:
            s2, addr = s.accept()
            executor.submit(servicio, s2, addr)
            #s2.close()


