'''
Created on 3 dic. 2023

@author: eliumontoya
'''

class TopologiaBus:
    def transmitir_datos(self, datos):
        print(f"Transmitiendo datos en topología de bus: {datos}")

class TopologiaEstrella:
    def transmitir_datos(self, datos):
        print(f"Transmitiendo datos en topología de estrella: {datos}")

# Uso de las topologías
bus = TopologiaBus()
estrella = TopologiaEstrella()

bus.transmitir_datos("Datos confidenciales")
estrella.transmitir_datos("Datos importantes")
