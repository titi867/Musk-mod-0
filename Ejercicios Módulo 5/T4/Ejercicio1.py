# Para resolver estos ejercicios debes usar el
# fichero csvcompany_sales_data.csv.
# Lee el beneficio total de todos los meses y
# muéstralo mediante un gráfico de líneas. Se
# proporcionan los datos del beneficio total de
# cada mes. El gráfico de líneas generado debe
# incluir las siguientes propiedades:
# Nombre de la etiqueta X = Número de mes
# Nombre de la etiqueta Y = Beneficio total

import pandas as pd
import matplotlib.pyplot as plt

def grafico_beneficios():

    df = pd.read_csv("Modulo5_company_sales_data-221102-123259.csv")

    lista_meses = df["month_number"]
    lista_beneficios = df["total_profit"]

    plt.plot(lista_meses, lista_beneficios, color='b', linestyle='-')
    plt.xlabel("Número de mes")
    plt.ylabel("Beneficio total")
    plt.title("Beneficio total por mes")

    plt.xticks(lista_meses)
    plt.yticks([100000, 200000, 300000, 400000, 500000])

    plt.show()

if __name__ == "__main__":
    grafico_beneficios()