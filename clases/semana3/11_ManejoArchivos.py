'''
Tema 11
Created on 3 dic. 2023

@author: eliumontoya
'''

# Crear un archivo y escribir en él
with open('mi_archivo.txt', 'w') as file:
    file.write('¡Hola, mundo!')

# Leer el contenido del archivo
with open('mi_archivo.txt', 'r') as file:
    contenido = file.read()
    print(contenido)
