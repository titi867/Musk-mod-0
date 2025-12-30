#Ordena todos los coches por la columna Precio.

import pandas as pd

def ordenar_precio():

    df = pd.read_csv('Modulo5_Automobile_data_limpio.csv')
    df_ordenado = df.sort_values(by='price')
    return df_ordenado

if __name__ == "__main__":
    df_ordenado = ordenar_precio()
    print(df_ordenado)

