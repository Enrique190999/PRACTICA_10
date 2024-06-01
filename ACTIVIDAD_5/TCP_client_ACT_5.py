from socket import *
import os

ServerPort = 4455
ServerName = '127.0.0.1'
BUFFER_SIZE = 1024  

def send_file(filename):

    if not os.path.isfile(filename):
        print(f"El fichero {filename} no se encontró.")
        return 
    
    with socket(AF_INET, SOCK_STREAM) as client_socket:
       
        client_socket.connect((ServerName, ServerPort))
        print(f"Conectado al servidor {ServerName}:{ServerPort}")

        try:
            client_socket.sendall(filename.encode())
            
            with open(filename, 'rb') as file:
                while True:
                    data = file.read(BUFFER_SIZE)
                    if not data:
                        break
                    client_socket.sendall(data)
            print("Fichero enviado correctamente.")
        
        except FileNotFoundError: 
            print(f"El fichero {filename} no se encontró.")
        except Exception as e:
            print(f"Ocurrió un error: {e}")

filename = input("Introduce el nombre del fichero a enviar: ")
send_file(filename)
