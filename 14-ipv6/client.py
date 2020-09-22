import socket

s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

s.connect(("www.python.org", 80))
s.send(b"GET / HTTP/1.1\r\nHost:www.python.org\r\n\r\n")
response = s.recv(1024)
print (response)
s.close()

