#!/usr/bin/python3
      
import http.server
import socketserver

PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.ForkingTCPServer(("", PORT), Handler)
print("serving at port", PORT)
httpd.serve_forever()
