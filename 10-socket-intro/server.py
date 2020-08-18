import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1",5000))
s.listen(1)
while True:
    s2,addr = s.accept()
    print (addr)
    enviado = s2.recv(1024)
    respuesta = enviado.decode().upper()
    s2.send(respuesta.encode())
    print (enviado)
    s2.close()

