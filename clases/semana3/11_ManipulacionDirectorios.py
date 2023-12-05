'''
Tema 11
Created on 3 dic. 2023

@author: eliumontoya
'''

import os

dir = "mi_directorio2"
archivo = dir+'/nuevo_archivo.txt'
# Crear un directorio
try:
    os.mkdir(dir)
except:
    print ("ya existia directorio")
# Listar contenido del directorio
contenido_directorio = os.listdir('mi_directorio')
print(f'Contenido del directorio: {contenido_directorio}')

# Crear un archivo dentro del directorio
file = open(archivo, 'w')
file.write('Contenido del nuevo archivo')
file.close()

print(f'Contenido del directorio: {contenido_directorio}')


# Eliminar un archivo dentro del directorio
os.remove(archivo)
