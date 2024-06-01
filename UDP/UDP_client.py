from socket import * 

ServerPort = 61000
ServerName = '127.0.0.1'

with socket(AF_INET,SOCK_DGRAM) as UDPSocketClient:
    mensaje = input("Escriba el mensaje a enviar");
    UDPSocketClient.sendto(mensaje.encode(),(ServerName,ServerPort))
    respuesta = UDPSocketClient.recv(2048)
    print(respuesta.decode())
    UDPSocketClient.close()