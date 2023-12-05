'''
Tema 12
Created on 3 dic. 2023

@author: eliumontoya
'''


# RAID 1 - Mirroring
disk_1 = [1, 2, 3, 4, 5]
disk_2 = [1, 2, 3, 4, 5]  # Duplicación inicial

def raid_1_read(block_number):
    return disk_1[block_number]  # Se lee desde el primer disco (podría ser el segundo también)

def raid_1_write(data, block_number):
    disk_1[block_number] = data
    disk_2[block_number] = data  # Se escribe en ambos discos

# Ejemplo de lectura y escritura

print ("Disco1, ", disk_1)
print ("Disco2, ", disk_2)

raid_1_write(100, 2)  # Escribir en el bloque 2
print(raid_1_read(2))  # Leer el bloque 2 desde el primer disco



print ("Disco1, ", disk_1)
print ("Disco2, ", disk_2)