#Cuenta el total de coches por empresa.

import pandas as pd

def contar_coches(df):
    conteo = df['company'].value_counts()
    return conteo

if __name__ == "__main__":

    df_coches = pd.read_csv('Modulo5_Automobile_data_limpio.csv')

    resultado = contar_coches(df_coches)

    print("Total de coches por empresa:")
    print(resultado)
