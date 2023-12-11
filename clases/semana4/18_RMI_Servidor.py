'''
Created on 11 dic. 2023

@author: eliumontoya
pip install Pyro4
'''


# Servidor
import Pyro4

@Pyro4.expose
class MiObjetoRemoto:
    def saludar(self, nombre):
        return f"Hola, {nombre}! Soy un objeto remoto."

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()
uri = daemon.register(MiObjetoRemoto)

ns.register("mi_objeto", uri)
print("Listo para aceptar peticiones.")
daemon.requestLoop()