# Crea una matriz de enteros 5X2 de un rango
# entre 100 y 200 tal que la diferencia entre cada
# elemento sea 10

import numpy as np

def info_array():

    mi_array = np.arange(100, 200, 10).reshape(5, 2)

    print("INFORMACIÓN DEL ARRAY:")
    print(mi_array)

if __name__ == "__main__":
    info_array()