#Encuentra el nombre de la empresa del coche más caro. Imprime el nombre de la empresa del coche 
# más caro y su precio.

import pandas as pd

def coche_mas_caro():

    df = pd.read_csv('Modulo5_Automobile_data_limpio.csv')

    coche_mas_caro = df.loc[df['price'].idxmax()]

    print(f"El coche más caro es de la empresa: {coche_mas_caro['company']}, "
      f"con un precio de: {coche_mas_caro['price']}")
    
if __name__ == "__main__":
    coche_mas_caro()