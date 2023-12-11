'''
Created on 11 dic. 2023

@author: eliumontoya
'''


import socket
import struct


multicast_group = '224.3.29.71'
server_address = ('', 11000)

multicast_port = 5007

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_address)

group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)


# Datos a enviar al grupo multicast
message = "Hola desde el emisor multicast"

try:
    # Enviar datos al grupo multicast
    print(f"Enviando mensaje '{message}' al grupo multicast")
    sock.sendto(message.encode('utf-8'), (multicast_group, multicast_port))
finally:
    sock.close()