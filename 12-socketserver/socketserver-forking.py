import socketserver
import os

class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024)
        print(self.client_address)
        print(self.data)
        print (os.getpid())
        self.request.sendall(self.data.upper())

server =  socketserver.ForkingTCPServer(("0.0.0.0", 5000), Handler)
server.serve_forever()
server.server_close()
