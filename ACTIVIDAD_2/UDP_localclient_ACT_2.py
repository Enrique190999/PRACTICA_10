from socket import *
from datetime import datetime, timezone

ServerPort = 6000
ServerName = '127.0.0.1'

with socket(AF_INET, SOCK_DGRAM) as UDPSocketClient:
   
    timeToSend = int(datetime.now(timezone.utc).timestamp() * 1000000)
    timeToSendBytes = timeToSend.to_bytes(8, 'little')
    
    UDPSocketClient.sendto(timeToSendBytes, (ServerName, ServerPort))
    
    data, server = UDPSocketClient.recvfrom(2048)
    recibido = int.from_bytes(data, 'little')
    
    print(f"Enviado: {timeToSend}")
    print(f"Recibido: {recibido}")
