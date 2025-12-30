# Lee los datos de las ventas de pasta de dientes
# de cada mes y muéstralos mediante un gráfico
# de dispersión (scatter). Además, añade una
# cuadrícula en el gráfico. El estilo de la cuadrícula
# debe ser "-".

import pandas as pd
import matplotlib.pyplot as plt

def ventas_pasta_dientes():

    datos = pd.read_csv('Modulo5_company_sales_data-221102-123259.csv')

    meses = datos['month_number']
    pasta = datos['toothpaste']

    plt.scatter(meses, pasta, marker='o', label='Venta de pasta de dientes')
    plt.xlabel('Número del mes')
    plt.ylabel('Número de unidades vendidas')
    plt.title('Ventas de pasta de dientes')
    plt.grid(linestyle='--', alpha=0.5)
    plt.legend(loc='upper left')
    plt.xticks(meses)
    plt.yticks(range(4500, 8500, 500))
    plt.show()

if __name__ == "__main__":
    ventas_pasta_dientes()


