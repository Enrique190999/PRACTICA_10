from socket import *

serverPortTCP = 12000

with socket(AF_INET,SOCK_STREAM) as serverSocketTCP:
    serverSocketTCP.bind(('',serverPortTCP))
    serverSocketTCP.listen(1)
    print('El servidor está listo para recibir datos')
    while True:
        connectionSocketTCP, addr = serverSocketTCP.accept()
        with connectionSocketTCP:
            print('Servidor conectado con la IP', addr[0], 'y puerto', addr[1])
            mensaje = connectionSocketTCP.recv(1024).decode()
            mensajeModificado = mensaje.upper()
            connectionSocketTCP.send(mensajeModificado.encode())
            connectionSocketTCP.close()