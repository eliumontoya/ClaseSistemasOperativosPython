'''
Tema 11
Created on 3 dic. 2023

@author: eliumontoya
'''


import os

# Obtener la ruta actual
ruta_actual = os.getcwd()
print(f'Ruta actual: {ruta_actual}')

# Crear una ruta absoluta para un archivo dentro de un directorio
ruta_archivo = os.path.join(ruta_actual, 'mi_directorio', 'archivo.txt')
print(f'Ruta absoluta del archivo: {ruta_archivo}')

# Obtener la ruta y el nombre del archivo por separado
nombre_archivo = os.path.basename(ruta_archivo)
ruta_sin_nombre = os.path.dirname(ruta_archivo)
print(f'Nombre del archivo: {nombre_archivo}')
print(f'Ruta sin nombre de archivo: {ruta_sin_nombre}')
