'''
Created on 22 nov. 2023

@author: eliumontoya
'''

import threading

def tarea(numero):
    print(f"Tarea {numero} ejecutándose")

threads = []

for i in range(5):
    thread = threading.Thread(target=tarea, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
