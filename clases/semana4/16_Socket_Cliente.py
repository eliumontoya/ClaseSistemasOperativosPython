'''
Created on 11 dic. 2023

@author: eliumontoya
'''

# Cliente
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8080))

response = client_socket.recv(1024)
print(response.decode())

client_socket.close()