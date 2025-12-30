# Ordena el siguiente array de NumPy:
# Caso 1: Ordenar el array por la segunda fila
# Caso 2: Ordenar el array por la segunda columna
# sampleArray = numpy.array([[34,43,73], [82,22,12], [53,94,66]])

import numpy as np

def ordenar_array():

    sampleArray = np.array([[34,43,73], [82,22,12], [53,94,66]])
    print("ARRAY ORIGINAL:")
    print(sampleArray)

    ordenar_segunda_fila = sampleArray[:, sampleArray[1, :].argsort()]
    print(f"\nEl array ordenado por la segunda fila es:\n{ordenar_segunda_fila}")

    ordenar_segunda_columna = sampleArray[sampleArray[:, 1].argsort(), :]
    print(f"\nEl array ordenado por la segunda columna es:\n{ordenar_segunda_columna}")

if __name__ == "__main__":
    ordenar_array()
