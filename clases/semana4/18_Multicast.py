'''
Created on 11 dic. 2023

@author: eliumontoya
'''


import socket
import struct


multicast_group = '224.3.29.71'
server_address = ('', 10000)
multicast_port = 5007


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(server_address)

group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
    print("\nEsperando recibir mensaje...")
    data, address = sock.recvfrom(5007 )
    print(f"Mensaje recibido desde {address}: {data.decode()}")