'''
Created on 11 dic. 2023

@author: eliumontoya
'''

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = []

    def agregar_conexion(self, nodo):
        self.conexiones.append(nodo)
        nodo.conexiones.append(self)

# Creación de nodos
nodo_a = Nodo("Nodo A")
nodo_b = Nodo("Nodo B")
nodo_c = Nodo("Nodo C")

# Establecimiento de conexiones entre nodos
nodo_a.agregar_conexion(nodo_b)
nodo_a.agregar_conexion(nodo_c)

# Mostrar conexiones de cada nodo
for nodo in [nodo_a, nodo_b, nodo_c]:
    print(f"Conexiones de {nodo.nombre}:")
    for conexion in nodo.conexiones:
        print(conexion.nombre)