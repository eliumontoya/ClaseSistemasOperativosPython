'''
Tema 14
Created on 3 dic. 2023

@author: eliumontoya
'''

import socket

url = 'www.ejemplo.com'
ip = socket.gethostbyname(url)
print(f'La dirección IP de {url} es: {ip}')
