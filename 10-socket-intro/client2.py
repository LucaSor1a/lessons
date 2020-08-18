import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("localhost", 5000))
s.send(b"hola server\n")
response = s.recv(1024)
print (response)
s.close()

