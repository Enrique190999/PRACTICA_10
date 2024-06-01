from socket import *
import threading

ServerPort = 4455
BUFFER_SIZE = 1024 

def handle_client(connection_socket, client_address):
    print(f"Conexión establecida con {client_address}")

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

    finally:
        connection_socket.close()

def start_server():
    with socket(AF_INET, SOCK_STREAM) as server_socket:
        server_socket.bind(('', ServerPort))
        server_socket.listen(5)
        print(f"Servidor escuchando en el puerto {ServerPort}")

        while True:
            connection_socket, client_address = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(connection_socket, client_address))
            client_thread.start()

start_server()
