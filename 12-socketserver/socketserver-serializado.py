import socketserver

class Handler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024)
        print(self.client_address)
        print(self.data)
        self.request.sendall(self.data.upper())

server =  socketserver.TCPServer(("0.0.0.0", 5000), Handler)
server.allow_reuse_address = True
server.serve_forever()

