#Escribe un programa en Python para comprobar si un archivo especificado existe.

import os

def existe_archivo(nombre_archivo):
    
    if os.path.isfile(nombre_archivo):
        print(f"El archivo '{nombre_archivo}' existe.")
    else:
        print(f"El archivo '{nombre_archivo}' NO existe.")

if __name__ == "__main__":
    existe_archivo("pilares_solid.txt")
    existe_archivo("archivo_imaginario.txt")