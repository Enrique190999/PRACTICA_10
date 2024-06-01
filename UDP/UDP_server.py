from socket import * 

ServerPort = 61000 

with socket(AF_INET, SOCK_DGRAM) as UDPServerSocket: 
    UDPServerSocket.bind(('', ServerPort))
    while True:
        mensaje, clientAddress = UDPServerSocket.recvfrom(2048)
        mensajeModificado = mensaje.decode().upper()
        print(mensajeModificado)
        UDPServerSocket.sendto(mensajeModificado.encode(), clientAddress)
