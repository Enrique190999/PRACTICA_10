from socket import *
from datetime import datetime, timezone

ServerPort = 61000
ServerName = 'isalabs.us.to'

with socket(AF_INET, SOCK_DGRAM) as UDPSocketClient:

    timeToSend = int(datetime.now(timezone.utc).timestamp() * 1000000)
    timeToSendBytes = timeToSend.to_bytes(8, 'little')
    
    UDPSocketClient.sendto(timeToSendBytes, (ServerName, ServerPort))
    
    data, server = UDPSocketClient.recvfrom(2048)
    recibido = int.from_bytes(data, 'little')
    
    print(f"Enviado: {timeToSend}")
    print(f"Recibido: {recibido}")
