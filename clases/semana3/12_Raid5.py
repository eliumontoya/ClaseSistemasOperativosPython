'''
Tema 12
Created on 3 dic. 2023

@author: eliumontoya
'''

# RAID 5 - Striping with Parity
disk_1 = [1, 2, 3, 4, 5]
disk_2 = [6, 7, 8, 9, 10]
disk_3 = [11, 12, 13, 14, 15]  # Disco de paridad

def raid_5_read(block_number):
    # Leer los bloques y calcular la paridad
    data = disk_1[block_number] ^ disk_2[block_number] ^ disk_3[block_number]
    return data

def raid_5_write(data, block_number):
    # Escribir en los discos y actualizar la paridad
    disk_1[block_number] = data
    disk_3[block_number] = disk_1[block_number] ^ disk_2[block_number]

# Ejemplo de lectura y escritura

print ("Disco1, ", disk_1)
print ("Disco2, ", disk_2)
print ("Disco3, ", disk_3)

raid_5_write(100, 1)  # Escribir en el bloque 1
print(raid_5_read(1))  # Leer el bloque 1



print ("Disco1, ", disk_1)
print ("Disco2, ", disk_2)
print ("Disco3, ", disk_3)
