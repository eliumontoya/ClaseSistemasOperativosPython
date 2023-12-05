'''

TEMA 8
Created on 27 nov. 2023

@author: eliumontoya
'''


class Proceso:
    def __init__(self, nombre, tiempo_llegada, tiempo_ejecucion):
        self.nombre = nombre
        self.tiempo_llegada = tiempo_llegada
        self.tiempo_ejecucion = tiempo_ejecucion

def planificacion_fcfs(procesos):
    tiempo_actual = 0

    for proceso in procesos:
        if tiempo_actual < proceso.tiempo_llegada:
            tiempo_actual = proceso.tiempo_llegada

        print(f"Ejecutando {proceso.nombre} desde {tiempo_actual} hasta {tiempo_actual + proceso.tiempo_ejecucion}")
        tiempo_actual += proceso.tiempo_ejecucion

# Crear procesos de prueba
p1 = Proceso("P1", 0, 8)
p2 = Proceso("P2", 1, 4)
p3 = Proceso("P3", 2, 9)

# Lista de procesos
procesos = [p1, p3, p2]

# Ejecutar planificación FCFS
print("Planificación FCFS:")
planificacion_fcfs(procesos)
