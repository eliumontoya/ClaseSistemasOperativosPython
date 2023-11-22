'''
Created on 22 nov. 2023

@author: eliumontoya
'''


import threading

def procesar_datos(datos):
    # Realizar algún procesamiento en los datos
    resultado = datos * 2
    print(f"Datos procesados: {resultado}")

datos_a_procesar = [1, 2, 3, 4, 5]
threads = []

for dato in datos_a_procesar:
    thread = threading.Thread(target=procesar_datos, args=(dato,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()


