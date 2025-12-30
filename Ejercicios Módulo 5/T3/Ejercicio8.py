# Imprime el máximo del eje 0 (columnas)y el mínimo del eje 1 (filas)
# de la siguiente matriz bidimensional:
# sampleArray = numpy.array([[34,43,73],[82,22,12], [53,94,66]])

import numpy as np

def max_min():

    sampleArray = np.array([[34,43,73],[82,22,12], [53,94,66]])
    print("ARRAY ORIGINAL:")
    print(sampleArray)

    max_eje_0 = np.amax(sampleArray, axis=0)
    min_eje_1 = np.amin(sampleArray, axis=1)

    print(f"\nEl máximo del eje 0 es: {max_eje_0}")
    print(f"El mínimo del eje 1 es: {min_eje_1}")

if __name__ == "__main__":
    max_min()
