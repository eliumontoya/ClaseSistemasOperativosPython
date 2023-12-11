'''
Created on 11 dic. 2023

@author: eliumontoya
'''
 #==============================================================================
 # Servidor
 #==============================================================================
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8080))
server_socket.listen(5)

print("Esperando conexiones...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Conexión entrante de {addr}")
    client_socket.send(b"Hola, cliente.  Conexion exitosa ")
    client_socket.close()