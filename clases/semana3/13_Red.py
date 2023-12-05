'''
Tema 13
Created on 3 dic. 2023

@author: eliumontoya
'''

class Red:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.dispositivos = []

    def agregar_dispositivo(self, dispositivo):
        self.dispositivos.append(dispositivo)

# Ejemplo de uso
red_local = Red('Red Local', 'LAN')
red_local.agregar_dispositivo('PC')
red_local.agregar_dispositivo('Impresora')

print(f'{red_local.nombre}: {red_local.dispositivos}')
