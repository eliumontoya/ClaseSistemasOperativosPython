'''
Created on 27 nov. 2023

@author: eliumontoya
'''
from abc import ABC, abstractmethod

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
        return "Leyendo desde el disco duro..."
    
    def write(self, data):
        return f"Escribiendo en el disco duro: {data}"

# Clase para la unidad flash USB que implementa la interfaz
class USBFlashDrive(StorageDevice):
    def read(self):
        return "Leyendo desde la unidad flash USB..."
    
    def write(self, data):
        return f"Escribiendo en la unidad flash USB: {data}"

# Uso de las clases
hd = HardDisk()
usb = USBFlashDrive()

print(hd.read())  # Salida: Leyendo desde el disco duro...
print(usb.write("Datos"))  # Salida: Escribiendo en la unidad flash USB: Datos
