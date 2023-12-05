'''
Tema 11
Created on 3 dic. 2023

@author: eliumontoya
'''

class NodoI:
    def __init__(self, nombre, tipo, propietario, tamaño, extension):
        self.nombre = nombre  # Nombre del archivo
        self.tipo = tipo  # Tipo de archivo (ejemplo: archivo, directorio)
        self.propietario = propietario  # Propietario del archivo
        self.tamaño = tamaño  # Tamaño del archivo en bytes
        self.extension = extension

    def __str__(self):
        return f"Nombre: {self.nombre}, Tipo: {self.tipo}, Propietario: {self.propietario}, Tamaño: {self.tamaño} bytes"


# Crear un nodo-i para un archivo
nodo_archivo = NodoI("documento.txt", "archivo", "user123", 1024, "exe")

# Mostrar las propiedades del archivo utilizando el nodo-i
print("Propiedades del archivo:")
print(nodo_archivo)
