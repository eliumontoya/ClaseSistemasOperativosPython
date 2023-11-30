'''
TEMA 9
Created on 29 nov. 2023

@author: eliumontoya
'''

# Simulación de lectura y escritura en un archivo usando búferes en Python
tamano_buffer = 5 
# Función para leer un archivo utilizando búferes
def leer_con_buffer(nombre_archivo):
     # Tamaño del búfer
    with open(nombre_archivo, 'r') as archivo:
        while True:
            datos = archivo.read(tamano_buffer)  # Lectura de datos con el tamaño del búfer
            if not datos:  # Si no hay más datos, se termina la lectura
                break
            print("Datos leídos:", datos)

# Función para escribir en un archivo utilizando búferes
def escribir_con_buffer(nombre_archivo, datos_a_escribir):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(datos_a_escribir)
    print("Datos escritos en el archivo.")

# Ejemplo de uso: escribir en un archivo y luego leerlo utilizando búferes
datos_para_escribir = "Esto es una prueba para el ejemplo de búferes en E/S."
nombre_archivo = "archivo_prueba.txt"

# Escribir en el archivo
escribir_con_buffer(nombre_archivo, datos_para_escribir)

# Leer el archivo utilizando búferes
print("\nLeyendo el archivo con búferes: ", tamano_buffer)
leer_con_buffer(nombre_archivo)
