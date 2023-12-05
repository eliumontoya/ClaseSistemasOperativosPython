'''
TEMA 9
Created on 27 nov. 2023

@author: eliumontoya
'''
from abc import ABC, abstractmethod


# TEMA 9
 
# Interfaz para el dispositivo de almacenamiento
class StorageDevice(ABC):
    @abstractmethod
    def read(self):
        pass
    
    @abstractmethod
    def write(self, data):
        pass

# Clase para el disco duro que implementa la interfaz
class HardDisk(StorageDevice):
    def read(self):
        return "Leyendo desde el disco duro... ffffffffff"
    
    def write(self, data):
        return f"Escribiendo en el disco duro: {data} 0x0x020230"

# Clase para la unidad flash USB que implementa la interfaz
class USBFlashDrive(StorageDevice):
    def read(self):
        return "Leyendo desde la unidad flash USB... 00000000000"
    
    def write(self, data):
        return f"Escribiendo en la unidad flash USB: {data} 0101010110101001"

# Uso de las clases
hd = HardDisk()
usb = USBFlashDrive()

print(hd.read())  # Salida: Leyendo desde el disco duro...
print(usb.read())  # Salida: Leyendo desde el disco duro...

print(hd.write("Datos"))  # Salida: Escribiendo en la unidad flash USB: Datos
print(usb.write("Datos"))  # Salida: Escribiendo en la unidad flash USB: Datos
