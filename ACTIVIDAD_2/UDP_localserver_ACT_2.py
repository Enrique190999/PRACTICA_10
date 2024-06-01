from socket import *
from datetime import datetime, timezone

ServerPort = 6000

with socket(AF_INET, SOCK_DGRAM) as UDPServerSocket:
    UDPServerSocket.bind(('', ServerPort))
    print(f"Servidor escuchando en el puerto {ServerPort}")

    while True:
        mensaje, clientAddress = UDPServerSocket.recvfrom(2048)
        
        timeToSend = int(datetime.now(timezone.utc).timestamp() * 1000000)
        timeToSendBytes = timeToSend.to_bytes(8, 'little')
        
        UDPServerSocket.sendto(timeToSendBytes, clientAddress)
        
        print(f"Mensaje recibido de {clientAddress}: {mensaje}")
        print(f"Tiempo enviado: {timeToSend}")

