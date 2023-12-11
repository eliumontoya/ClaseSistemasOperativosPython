'''
Created on 11 dic. 2023

@author: eliumontoya
'''

# Servidor RPC
from xmlrpc.server import SimpleXMLRPCServer

def add(x, y):
    return x + y

server = SimpleXMLRPCServer(('127.0.0.1', 8000))
server.register_function(add, 'addition')

print("Servidor RPC en funcionamiento en el puerto 8000...")
server.serve_forever()