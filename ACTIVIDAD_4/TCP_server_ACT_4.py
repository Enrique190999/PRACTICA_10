from socket import *
import os

ServerPort = 4455
BUFFER_SIZE = 1024 

def start_server():
    with socket(AF_INET, SOCK_STREAM) as server_socket:
        server_socket.bind(('', ServerPort))
        server_socket.listen(5)
        print(f"Servidor escuchando en el puerto {ServerPort}")

        while True:
            connection_socket, client_address = server_socket.accept()
            print(f"Conexión establecida con {client_address}")

            with connection_socket:
                try:
                    filename = connection_socket.recv(BUFFER_SIZE).decode()
                    print(f"Nombre del fichero recibido: {filename}")
                   
                    with open(filename, 'wb') as file:
                        while True:
                            data = connection_socket.recv(BUFFER_SIZE)
                            if not data:
                                break
                            file.write(data)
                    print(f"Fichero {filename} guardado correctamente en {filename}")

                except Exception as e:
                    print(f"Ocurrió un error: {e}")

start_server()
