'''
Tema 11
Created on 3 dic. 2023

@author: eliumontoya
'''

import os

# Crear un directorio
os.mkdir('mi_directorio')

# Listar contenido del directorio
contenido_directorio = os.listdir('mi_directorio')
print(f'Contenido del directorio: {contenido_directorio}')

# Crear un archivo dentro del directorio
with open('mi_directorio/nuevo_archivo.txt', 'w') as file:
    file.write('Contenido del nuevo archivo')

# Eliminar un archivo dentro del directorio
os.remove('mi_directorio/nuevo_archivo.txt')
