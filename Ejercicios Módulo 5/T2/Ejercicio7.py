#Encuentra el kilometraje medio de cada empresa fabricante de automóviles.

import pandas as pd

def kilometraje_medio_por_empresa(df):

    resultado = df.groupby('company')['average-mileage'].mean()
    return resultado

if __name__ == "__main__":

    df_coches = pd.read_csv('Modulo5_Automobile_data_limpio.csv')

    resultado = kilometraje_medio_por_empresa(df_coches)

    print("Kilometraje medio por empresa:")
    print(resultado)