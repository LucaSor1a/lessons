#!/usr/bin/python3

import socketserver

class TcpHilos(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class Maneja(socketserver.BaseRequestHandler):
    def setup(self):
        print("inicio", self.client_address)
    def handle(self):
        self.data = self.request.recv(1024)
        print (self.data)
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    endpoint = ("0.0.0.0", 6000)
#    servidor = socketserver.ThreadingTCPServer(endpoint, Maneja)
    servidor = TcpHilos(endpoint,Maneja)
    servidor.allow_reuse_address = True
    servidor.serve_forever()
