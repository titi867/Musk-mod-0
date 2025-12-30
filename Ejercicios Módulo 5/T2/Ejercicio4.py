#Imprime todos los datos de los coches Toyota.

import pandas as pd

def coches_toyota():

    df = pd.read_csv('Modulo5_Automobile_data_limpio.csv')

    coches_toyota = df[df['company'] == 'toyota']

    print("Datos de los coches Toyota:")
    print(coches_toyota)

if __name__ == "__main__":
    coches_toyota()