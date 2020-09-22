import socket
servidor = "www.google.com"
direcciones = socket.getaddrinfo(servidor, 80,  0 , 1 )

for direccion in direcciones:
    s = socket.socket(direccion[0], direccion[1])
#    s = socket.socket(direcciones[0], socket.SOCK_STREAM)
    print ("me conecto a:", direccion[4] )
    s.connect((direccion[4]))
    s.send(bytearray("GET / HTTP/1.1\r\nHost:" + servidor + "\r\n\r\n","utf-8"))
    response = s.recv(1024)
    print (response)
    s.close()

