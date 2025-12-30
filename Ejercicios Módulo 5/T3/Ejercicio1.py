# Crea un array de enteros 4X2 e imprime sus
# atributos. Nota: El elemento debe ser de tipo
# unsignedint16. Imprime los siguientes atributos:
# La shape del array.
# Las dimensiones del array.
# El tamaño de cada elemento del array en bytes.

import numpy as np

def info_array():

    mi_array = np.empty([4, 2], dtype=np.uint16)

    print("INFORMACIÓN DEL ARRAY:")
    print(mi_array)

    print("Shape del array:", mi_array.shape)
    print("Dimensiones del array:", mi_array.ndim)
    print("Tamaño de cada elemento en bytes:", mi_array.itemsize)

if __name__ == "__main__":
    info_array()