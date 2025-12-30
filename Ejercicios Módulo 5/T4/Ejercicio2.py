# Obtenga el beneficio total de todos los meses y muestre un gráfico de líneas con las siguientes
# propiedades de estilo:
# •Estilo de línea punteada y el color de la línea debe ser rojo
# •Mostrar la leyenda en la parte inferior derecha.
# •Nombre de la etiqueta X = Número de mes
# •Nombre de la etiqueta Y = Número de unidades vendidas
# •Añadir un marcador de círculo.
# •El ancho de la línea debe ser 3
# He puesto las etiquetas de la imagen, no los de la instrucción 

import pandas as pd
import matplotlib.pyplot as plt

def beneficio_total():

    df = pd.read_csv("Modulo5_company_sales_data-221102-123259.csv")

    lista_meses = df["month_number"]
    lista_unidades_vendidas = df["total_profit"]

    plt.plot(lista_meses, lista_unidades_vendidas, color='r', linestyle='--', marker='o', markerfacecolor= 'k',
             linewidth=3, label='Profit data of last year')

    plt.xlabel("Número de mes")
    plt.ylabel("Beneficio total")
    plt.title("Beneficios por mes")
    plt.legend(loc='lower right')
    plt.xticks(lista_meses)
    plt.yticks([100000, 200000, 300000, 400000, 500000])
    plt.show()

if __name__ == "__main__":
    beneficio_total()
