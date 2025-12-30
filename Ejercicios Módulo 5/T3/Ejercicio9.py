# Elimina la segunda columna de una matriz dada е
# inserta la siguiente columna nueva en su lugar.
# sampleArray = numpy.array([[34,43,73], [82,22,12],[53,94,66]])
# newColumn = numpy.array([[10,10,10]])

import numpy as np

def editar_columna():

    sampleArray = np.array([[34,43,73], [82,22,12],[53,94,66]])
    newColumn = np.array([[10,10,10]])

    print("ARRAY ORIGINAL:")
    print(sampleArray)

    sampleArray = np.delete(sampleArray, 1, axis=1)
    sampleArray = np.insert(sampleArray, 1, newColumn, axis=1)

    print("\nARRAY MODIFICADO:")
    print(sampleArray)

if __name__ == "__main__":
    editar_columna()