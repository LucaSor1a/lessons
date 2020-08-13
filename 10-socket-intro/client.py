import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("www.um.edu.ar", 80))
s.send(b"GET / HTTP/1.1\r\nHost:www.um.edu.ar\r\n\r\n")
response = s.recv(1024)
print (response)
s.close()

