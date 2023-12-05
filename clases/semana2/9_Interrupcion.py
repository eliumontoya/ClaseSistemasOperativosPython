'''
TEMA 9
Created on 29 nov. 2023

@author: eliumontoya
'''

import signal
import time

# Función para manejar la señal de interrupción (Ctrl+C)
def manejador_interrupcion(signal, frame):
    print("\n¡Se ha recibido una señal de interrupción (Ctrl+C)!")
    exit(0)

# Asociar la señal SIGINT (Ctrl+C) al manejador_interrupcion
signal.signal(signal.SIGINT, manejador_interrupcion)

print("El programa está en ejecución. Presiona Ctrl+C para detenerlo.")

# Simulación de un bucle que se ejecuta indefinidamente
while True:
    print("El programa sigue en ejecución...")
    time.sleep(2)  # Espera de 2 segundos entre cada iteración del bucle
