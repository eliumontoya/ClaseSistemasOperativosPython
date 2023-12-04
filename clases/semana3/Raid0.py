'''
Tema 12
Created on 3 dic. 2023

@author: eliumontoya
'''


# RAID 0 - Striping
disk_1 = [1, 2, 3, 4, 5]
disk_2 = [6, 7, 8, 9, 10]

def raid_0_read(block_number):
    if block_number < len(disk_1):
        return disk_1[block_number]
    else:
        return disk_2[block_number - len(disk_1)]

def raid_0_write(data, block_number):
    if block_number < len(disk_1):
        disk_1[block_number] = data
    else:
        disk_2[block_number - len(disk_1)] = data

# Ejemplo de lectura y escritura
Bloque = 3

print ("Disco1, ", disk_1)
print ("Disco2, ", disk_2)
raid_0_write(15340, Bloque)  # Escribir en el bloque 3
print(raid_0_read(Bloque))  # Leer el bloque 3

print ("Disco1, ", disk_1)
print ("Disco2, ", disk_2)