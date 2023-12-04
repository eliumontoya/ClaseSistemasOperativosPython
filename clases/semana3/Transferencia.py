'''
Created on 3 dic. 2023

@author: eliumontoya
'''

import time

def transferir_datos(origen, destino, datos):
    print(f'Transfiriendo datos desde {origen} a {destino}: {datos}')
    time.sleep(2)
    print('Transferencia completa')

# Uso de la función
transferir_datos('Nodo A', 'Nodo B', 'Datos importantes')
