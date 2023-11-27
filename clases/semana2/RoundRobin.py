'''
Created on 27 nov. 2023

@author: eliumontoya
'''

class Proceso:
    def __init__(self, nombre, tiempo_llegada, tiempo_ejecucion):
        self.nombre = nombre
        self.tiempo_llegada = tiempo_llegada
        self.tiempo_ejecucion = tiempo_ejecucion

def planificacion_rr(procesos, quantum):
    tiempo_actual = 0
    procesos_restantes = procesos.copy()

    while procesos_restantes:
        proceso_actual = procesos_restantes.pop(0)
        print(f"Ejecutando {proceso_actual.nombre} desde {tiempo_actual} hasta ", end="")
        
        if proceso_actual.tiempo_ejecucion > quantum:
            print(f"{tiempo_actual + quantum} (Quantum expirado)")
            proceso_actual.tiempo_ejecucion -= quantum
            tiempo_actual += quantum
            procesos_restantes.append(proceso_actual)
        else:
            print(f"{tiempo_actual + proceso_actual.tiempo_ejecucion} (Proceso completado)")
            tiempo_actual += proceso_actual.tiempo_ejecucion

# Crear procesos de prueba
p1 = Proceso("P1", 0, 8)
p2 = Proceso("P2", 1, 4)
p3 = Proceso("P3", 2, 9)

# Lista de procesos
procesos = [p1, p2, p3]

# Ejecutar planificación RR con quantum de 5
print("Planificación RR:")
planificacion_rr(procesos, 5)