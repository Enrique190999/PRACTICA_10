from socket import *
from datetime import datetime, timezone

# Obtener el tiempo actual en microsegundos
timeToSend = int(datetime.now(timezone.utc).timestamp() * 1000000)

ServerPort = 61000
ServerName = '127.0.0.1'

with socket(AF_INET, SOCK_DGRAM) as UDPSocketClient:
    timeToSendBytes = timeToSend.to_bytes(8, 'little')
    UDPSocketClient.sendto(timeToSendBytes, (ServerName, ServerPort))
    
    data, server = UDPSocketClient.recvfrom(2048)
    
    recibido = int.from_bytes(data, 'little')
    
    print(f"Enviado: {timeToSend}")
    print(f"Recibido: {recibido}")
