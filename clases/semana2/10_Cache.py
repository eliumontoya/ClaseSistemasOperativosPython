'''
TEMA 10
Created on 29 nov. 2023

@author: eliumontoya
'''
from collections import OrderedDict

class MemoriaCache:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.cache = OrderedDict()

    def acceder_elemento(self, elemento):
        if elemento in self.cache:
            # Mover el elemento al final para denotar su uso reciente
            self.cache.move_to_end(elemento)
        else:
            if len(self.cache) >= self.capacidad:
                # Eliminar el elemento menos reciente (el primero en orden)
                self.cache.popitem(last=False)
            self.cache[elemento] = True  # Podría ser cualquier valor

    def mostrar_cache(self):
        print("Elementos en caché (de más reciente a menos):")
        for elemento in reversed(self.cache):
            print(elemento)


# Uso del sistema de memoria caché
cache = MemoriaCache(3)
cache.acceder_elemento("A")
cache.acceder_elemento("B")
cache.acceder_elemento("C")
cache.mostrar_cache()

cache.acceder_elemento("D")  # Se agrega "D" y "A" se elimina por ser el menos reciente
cache.mostrar_cache()

cache.acceder_elemento("C")  # Acceso a "C", lo mueve al final
cache.mostrar_cache()
