#Para realizar los ejercicios, usar el archivo csvAutomobile_data.csv. A partir del conjunto de datos dado, 
# imprime las cinco primeras y últimas filas.

import pandas as pd

def mostrar_filas():
    df = pd.read_csv("Modulo5_Automobile_data-221102-123259.csv")

    print("Primeras cinco filas:")
    print(df.head(5))

    print("\nÚltimas cinco filas:")
    print(df.tail(5))

if __name__ == "__main__":
   mostrar_filas()