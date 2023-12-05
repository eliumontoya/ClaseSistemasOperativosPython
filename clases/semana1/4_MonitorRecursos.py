'''
Tema 4
Created on 22 nov. 2023

@author: eliumontoya
'''

import psutil
import tkinter as tk

def actualizar_datos():
    cpu_percent = psutil.cpu_percent(interval=1)
    mem_info = psutil.virtual_memory()

    lbl_cpu.config(text=f"CPU: {cpu_percent}%")
    lbl_mem.config(text=f"Memoria: {mem_info.percent}%")

    root.after(1000, actualizar_datos)  # Actualizar cada 1 segundo

root = tk.Tk()
lbl_cpu = tk.Label(root, text="CPU:")
lbl_cpu.pack()
lbl_mem = tk.Label(root, text="Memoria:")
lbl_mem.pack()

actualizar_datos()
root.mainloop()

