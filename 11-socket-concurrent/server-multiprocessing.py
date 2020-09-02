import socket
import multiprocessing
import signal

def servicio(s2,addr):
    print (addr)
    enviado = s2.recv(1024)
    respuesta = enviado.decode().upper()
    s2.send(respuesta.encode())
    print (enviado)
    s2.close()

# no quiero zombiessss
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# otra vez .... address already in use 
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("127.0.0.1",5000))
s.listen(1)
while True:
    s2,addr = s.accept()
    hijo = multiprocessing.Process(target=servicio, args = (s2,addr,))
    hijo.start()
    hijo.join()
    # descriptores abiertos ...
    #sudo lsof  -p 163748
    s2.close()
