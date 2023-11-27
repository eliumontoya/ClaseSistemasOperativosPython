'''
Created on 27 nov. 2023

@author: eliumontoya
'''

class Proceso:
    def __init__(self, numero):
        self.numero = numero

# Simulación de swapping
memoria_principal = [Proceso(i) for i in range(4)]  # Memoria principal con 4 procesos
memoria_secundaria = [Proceso(i) for i in range(8)]  # Memoria secundaria con 8 procesos

# Simular swapping de un proceso de memoria principal a memoria secundaria
proceso_a_swapping = memoria_principal.pop(2)  # Se selecciona el proceso 2 para swapping
memoria_secundaria.append(proceso_a_swapping)

# Mostrar el estado de la memoria principal y secundaria después del swapping
print("Memoria Principal:")
for proceso in memoria_principal:
    print(f"Proceso {proceso.numero}")

print("\nMemoria Secundaria:")
for proceso in memoria_secundaria:
    print(f"Proceso {proceso.numero}")