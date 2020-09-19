#!/usr/bin/python3
import socketserver

class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024)
        print(self.client_address)
        print(self.data)
        self.request.sendall(self.data.upper())

socketserver.TCPServer.allow_reuse_address = True
server =  socketserver.TCPServer(("0.0.0.0", 5000), Handler)
server.serve_forever()

