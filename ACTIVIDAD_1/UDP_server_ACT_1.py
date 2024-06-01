from socket import *
from datetime import datetime, timezone

ServerPort = 61000

with socket(AF_INET, SOCK_DGRAM) as UDPServerSocket:
    UDPServerSocket.bind(('', ServerPort))
    print(f"Servidor escuchando en el puerto {ServerPort}")

    while True:
        mensaje, clientAddress = UDPServerSocket.recvfrom(2048)
        timeReceived = int.from_bytes(mensaje, 'little')
        timeToSend = int(datetime.now(timezone.utc).timestamp() * 1000000)

        print(f'Tiempo desde el cliente: {timeReceived}, tiempo desde el servidor: {timeToSend}')
        
        timeToSendBytes = int.to_bytes(timeToSend, 'little')
        UDPServerSocket.sendto(timeToSendBytes, clientAddress)
