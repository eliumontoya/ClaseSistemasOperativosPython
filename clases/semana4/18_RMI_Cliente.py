'''
Created on 11 dic. 2023

@author: eliumontoya
'''

# Cliente
import Pyro4

uri = "PYRONAME:mi_objeto"
mi_objeto = Pyro4.Proxy(uri)

respuesta = mi_objeto.saludar("Cliente")
print(respuesta)