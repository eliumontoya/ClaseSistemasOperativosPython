'''
Created on 22 nov. 2023

@author: eliumontoya
'''


import threading
import time

recurso_1 = threading.Lock()
recurso_2 = threading.Lock()

def proceso_1():
    with recurso_1:
        time.sleep(1)
        with recurso_2:
            print("Proceso 1 ha obtenido ambos recursos")

def proceso_2():
    with recurso_2:
        time.sleep(1)
        with recurso_1:
            print("Proceso 2 ha obtenido ambos recursos")

thread_1 = threading.Thread(target=proceso_1)
thread_2 = threading.Thread(target=proceso_2)

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()
