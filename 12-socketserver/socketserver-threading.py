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
server =  socketserver.ThreadingTCPServer(("0.0.0.0", 5000), Handler)
server.allow_reuse_address = True
server.serve_forever()

