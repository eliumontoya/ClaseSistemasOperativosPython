'''
Tema 12
Created on 3 dic. 2023

@author: eliumontoya
'''

# Datos en los discos
disco1 = 0b10101101
disco2 = 0b11011010
disco3 = 0b01010111
disco4 = 0b11100011

# Calculando la paridad
paridad = disco1 ^ disco2 ^ disco3 ^ disco4

# Mostrando los datos y la paridad
print(f"Disco 1: {bin(disco1)}")
print(f"Disco 2: {bin(disco2)}")
print(f"Disco 3: {bin(disco3)}")
print(f"Disco 4: {bin(disco4)}")
print(f"Paridad : {bin(paridad)}")
