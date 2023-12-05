'''
Tema 11
Created on 3 dic. 2023

@author: eliumontoya
'''

# Escribir datos binarios en un archivo
with open('datos.bin', 'wb') as file:
    # Crear datos binarios (en este caso, bytes)
    datos_binarios = bytes([0b01010100, 0b00110011, 0b11110000])

    # Escribir los datos binarios en el archivo
    file.write(datos_binarios)
    print("Datos binarios escritos correctamente en el archivo 'datos.bin'")

# Leer datos binarios desde un archivo
with open('datos.bin', 'rb') as file:
    # Leer los datos binarios del archivo
    datos_leidos = file.read()

    # Mostrar los datos binarios leídos
    print("Datos binarios leídos del archivo 'datos.bin':", datos_leidos)

    # Mostrar los datos binarios como valores enteros
    valores_enteros = [int(byte) for byte in datos_leidos]
    print("Valores enteros de los datos binarios:", valores_enteros)
