from socket import *

serverName = '127.0.0.1'
serverPort = 12000

with socket(AF_INET, SOCK_STREAM) as clientSocketTCP:
    clientSocketTCP.connect((serverName,serverPort))
    mensaje = input('Escriba una frase en minúscula: ')
    clientSocketTCP.send(mensaje.encode())
    mensajeModificado = clientSocketTCP.recv(1024)
    print('From Server: ', mensajeModificado.decode())
    clientSocketTCP.close()