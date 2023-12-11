'''
Created on 11 dic. 2023

@author: eliumontoya
'''


from multiprocessing import Process, Queue

# Función que realiza un cálculo simple y pone el resultado en la cola de mensajes
def calcular_cuadrado(numero, cola):
    resultado = numero * numero
    cola.put(resultado)

if __name__ == '__main__':
    # Creamos una cola de mensajes para la comunicación entre procesos
    cola = Queue()

    # Creamos un proceso que realizará el cálculo
    proceso = Process(target=calcular_cuadrado, args=(5, cola))

    # Iniciamos el proceso
    proceso.start()

    # Esperamos a que el proceso termine y obtenemos el resultado de la cola
    proceso.join()
    resultado = cola.get()
    print("El resultado es:", resultado)