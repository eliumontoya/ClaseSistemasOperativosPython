'''
Tema 12
Created on 3 dic. 2023

@author: eliumontoya
'''
# RAID 10 - Combination of RAID 1 and RAID 0
disk_1 = [1, 2, 3, 4, 5]
disk_2 = [6, 7, 8, 9, 10]
mirror_disk_1 = list(disk_1)  # Duplicación de disco 1
mirror_disk_2 = list(disk_2)  # Duplicación de disco 2

def raid_10_read(block_number):
    if block_number < len(disk_1):
        return mirror_disk_1[block_number]
    else:
        return mirror_disk_2[block_number - len(disk_1)]

def raid_10_write(data, block_number):
    if block_number < len(disk_1):
        disk_1[block_number] = data
        mirror_disk_1[block_number] = data
    else:
        disk_2[block_number - len(disk_1)] = data
        mirror_disk_2[block_number - len(disk_1)] = data

# Ejemplo de lectura y escritura

print ("Disco1, ", disk_1)
print ("Disco2, ", disk_2)
print ("mirror_disk_1, ", mirror_disk_1)
print ("mirror_disk_2, ", mirror_disk_2)
raid_10_write(100, 4)  # Escribir en el bloque 4
print(raid_10_read(4))  # Leer el bloque 4


print ("Disco1, ", disk_1)
print ("Disco2, ", disk_2)
print ("mirror_disk_1, ", mirror_disk_1)
print ("mirror_disk_2, ", mirror_disk_2)