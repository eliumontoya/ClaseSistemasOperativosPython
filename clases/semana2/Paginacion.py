'''
Created on 27 nov. 2023

@author: eliumontoya
'''

class Pagina:
    def __init__(self, numero):
        self.numero = numero
        self.contenido = f'Contenido de la página {self.numero}'

class Proceso:
    def __init__(self, numero, paginas):
        self.numero = numero
        self.paginas = [Pagina(numero + i) for i in range(paginas)]

# Simulación de paginación
paginas_fisicas = [None] * 4  # Memoria física con 4 marcos
procesos = [Proceso(i, 2) for i in range(3)]  # Crear 3 procesos, cada uno con 2 páginas

# Asignar páginas a la memoria física
for proceso in procesos:
    for i, pagina in enumerate(proceso.paginas):
        marco = i % len(paginas_fisicas)  # Se simula el reemplazo de páginas
        paginas_fisicas[marco] = pagina
        print(f'Página {pagina.numero} del proceso {proceso.numero} en marco {marco}')

# Mostrar contenido de las páginas en la memoria física
for marco, pagina in enumerate(paginas_fisicas):
    if pagina:
        print(f'Marco {marco}: {pagina.contenido}')
    else:
        print(f'Marco {marco}: Vacío')
        