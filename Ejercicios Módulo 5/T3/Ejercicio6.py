# Divide la matriz en cuatro submatrices de igual
# tamaño. Nota: Crea una matriz de enteros 8x3
# de un rango entre 10 y 34 de tal manera que la
# diferencia entre cada elemento sea 1 y luego
# divide la matriz en cuatro submatrices de igual
# tamaño

import numpy as np

def submatrices():
    
    matriz = np.arange(10, 34, 1).reshape(8, 3)

    lista_submatrices = np.split(matriz, 4)

    print("MATRIZ ORIGINAL:")
    print(matriz)

    print("\nSUBMATRICES:")

    print(f"Submatriz 1:\n{lista_submatrices[0]}")
    print(f"Submatriz 2:\n{lista_submatrices[1]}")
    print(f"Submatriz 3:\n{lista_submatrices[2]}")
    print(f"Submatriz 4:\n{lista_submatrices[3]}")

if __name__ == "__main__":
    submatrices()
