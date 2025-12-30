# Devuelve un array de filas impares y columnas
# pares dado el siguiente array:
# sampleArray = numpy.array([[3,6, 9, 12], [15,18, 21, 24],
# [27,30, 33, 36], [39,42, 45, 48], [51,54, 57, 60]])

import numpy as np

def array_filas_impares_columnas_pares():
    sampleArray = np.array([[3,6, 9, 12], [15,18, 21, 24],
                            [27,30, 33, 36], [39,42, 45, 48],
                            [51,54, 57, 60]])
    filas_impares_columnas_pares = sampleArray[0::2, 1::2]
    print(filas_impares_columnas_pares)

if __name__ == "__main__":
    array_filas_impares_columnas_pares()