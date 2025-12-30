#Limpia el conjunto de datos y actualiza el archivo CSV. Reemplaza todos los valores de las columnas 
# que contengan ?, n.a., o NaN.

import pandas as pd

def limpiar_datos():

    df = pd.read_csv('Modulo5_Automobile_data-221102-123259.csv', na_values=["?", "n.a"])

    print("Datos limpios: ")
    print(df)

    df.to_csv('Modulo5_Automobile_data_limpio.csv', index=False)
    print("\n¡Archivo 'Automobile_data.csv' actualizado y limpio!")

if __name__ == "__main__":
    limpiar_datos()