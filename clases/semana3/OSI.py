'''
Created on 3 dic. 2023

@author: eliumontoya
'''
class CapaOSI:
    capas = {
        1: "Físico",
        2: "Enlace",
        3: "Red",
        4: "Transporte",
        5: "Sesión",
        6: "Presentación",
        7: "Aplicación"
    }

    def transmitir(self, mensaje):
        capa_actual = 1
        for capa_num in range(1, 8):
            print(f"Capa {capa_num} ({self.capas[capa_num]})")

            # Identificación del protocolo o tecnología
            if capa_actual == 1:
                print("Protocolo físico: Ethernet")
            elif capa_actual == 2:
                print("Protocolo de enlace: ARP")
            elif capa_actual == 3:
                print("Protocolo de red: IPv4")
            elif capa_actual == 4:
                print("Protocolo de transporte: TCP")
            elif capa_actual == 5:
                print("Protocolo de sesión: TCP")
            elif capa_actual == 6:
                print("Protocolo de presentación: SSL")
            elif capa_actual == 7:
                print("Protocolo de aplicación: HTTP")

            capa_actual += 1

# Mensaje a transmitir
mensaje = "¡Hola, mundo!"

# Crear objeto CapaOSI y transmitir el mensaje a través de las capas
modelo_osi = CapaOSI()
print(f"Transmitiendo mensaje - {mensaje} ")

modelo_osi.transmitir(mensaje)
