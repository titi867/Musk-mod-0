#Encuentra el coche con el precio más alto de precio de cada empresa.

import pandas as pd

def coche_mas_caro_por_empresa(df):

    resultado = df.loc[df.groupby('company')['price'].idxmax()]
    return resultado

if __name__ == "__main__":

    df_coches = pd.read_csv('Modulo5_Automobile_data_limpio.csv')

    resultado = coche_mas_caro_por_empresa(df_coches)

    print("Coche más caro por empresa:")
    print(resultado)