'''
Created on 27 nov. 2023

@author: eliumontoya
'''

class Segmento:
    def __init__(self, numero):
        self.numero = numero
        self.tamanio = numero * 2

class Proceso:
    def __init__(self, numero, segmentos):
        self.numero = numero
        self.segmentos = [Segmento(numero + i) for i in range(segmentos)]

# Simulación de segmentación
segmentos = []
procesos = [Proceso(i, 2) for i in range(3)]  # Crear 3 procesos, cada uno con 2 segmentos

# Asignar segmentos a los procesos
for proceso in procesos:
    for segmento in proceso.segmentos:
        segmentos.append(segmento)
        print(f'Segmento {segmento.numero} del proceso {proceso.numero} con tamaño {segmento.tamanio}')

# Mostrar todos los segmentos y sus tamaños
for segmento in segmentos:
    print(f'Segmento {segmento.numero} con tamaño {segmento.tamanio}')