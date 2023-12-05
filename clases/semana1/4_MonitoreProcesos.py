'''
Tema 4
Created on 22 nov. 2023

@author: eliumontoya
'''
import psutil

def mostrar_procesos():
    procesos = psutil.process_iter()
    for proceso in procesos:
        print(proceso.name(), proceso.pid)  # Mostrar nombre y PID

def finalizar_proceso(pid):
    proceso = psutil.Process(pid)
    proceso.terminate()  # Finalizar el proceso con el PID dado
 

mostrar_procesos()