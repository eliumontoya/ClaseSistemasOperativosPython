'''
Created on 11 dic. 2023

@author: eliumontoya
'''

# Cliente RPC
import xmlrpc.client

client = xmlrpc.client.ServerProxy('http://127.0.0.1:8000')
result = client.addition(5, 3)
print("Resultado de la adición:", result)
