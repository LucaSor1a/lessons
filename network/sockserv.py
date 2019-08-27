#!/usr/bin/python3

import socketserver

class Maneja(socketserver.BaseRequestHandler):
    def setup(self):
        print("inicio")
    def handle(self):
        self.data = self.request.recv(1024)
        print (self.data)
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    endpoint = ("0.0.0.0", 6000)
    servidor = socketserver.TCPServer(endpoint, Maneja)
    servidor.serve_forever()
