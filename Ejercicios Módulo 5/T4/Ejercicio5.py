# Lee los datos de ventas de los productos crema
# facial y lavado de cara y muéstralos mediante el
# gráfico barras. El gráfico de barras debe mostrar
# el número de unidades vendidas por mes para
# cada producto. Añade de una barra distinta para
# cada producto en el mismo gráfico.

import pandas as pd
import matplotlib.pyplot as plt

def ventas_cara():

    datos = pd.read_csv('Modulo5_company_sales_data-221102-123259.csv')
    
    meses = datos['month_number']
    crema_facial = datos['facecream']
    lavado_cara = datos['facewash']

    plt.bar(meses - 0.2, crema_facial, width=0.4, label='Ventas crema facial', align='center')
    plt.bar(meses + 0.2, lavado_cara, width=0.4, label='Ventas lavado de cara', align='center')

    plt.xlabel('Número del mes')
    plt.ylabel('Unidades de ventas en número')
    plt.title('Facewash and Facecream sales data')
    plt.legend(loc='upper left')
    plt.xticks(meses)
    plt.yticks(range(500, 4000, 500))
    plt.grid(linestyle='--', alpha=0.5)
    plt.show()

if __name__ == "__main__":
    ventas_cara()


