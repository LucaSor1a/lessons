#!/usr/bin/python3
import socketserver
#class HiloTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
#    pass

class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024)
        print(self.client_address)
        print(self.data)
        self.request.sendall(self.data.upper())

#server =  HiloTCPServer(("0.0.0.0", 5000), Handler)
socketserver.ThreadingTCPServer.allow_reuse_address = True
server =  socketserver.ThreadingTCPServer(("0.0.0.0", 5000), Handler)
server.serve_forever()

