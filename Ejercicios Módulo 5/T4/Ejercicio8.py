# Calcula los datos de ventas totales del último
# año para cada producto y muéstralos mediante
# un gráfico circular.Nota: En el gráfico circular
# muestra el número de unidades vendidas por año
# para cada producto en porcentaje.

import pandas as pd
import matplotlib.pyplot as plt

def ventas_anuales():

    datos = pd.read_csv('Modulo5_company_sales_data-221102-123259.csv')

    ventas_crema = datos['facecream'].sum()
    ventas_lavado = datos['facewash'].sum()
    ventas_pasta = datos['toothpaste'].sum()
    ventas_jabon = datos['bathingsoap'].sum()
    ventas_shampoo = datos['shampoo'].sum()
    ventas_hidratante = datos['moisturizer'].sum()

    eje_y = [ventas_crema, ventas_lavado, ventas_pasta, ventas_jabon, ventas_shampoo, ventas_hidratante]

    etiquetas = ['Crema facial', 'Lavado de cara', 'Pasta de dientes', 'Gel de baño', 'Shampoo', 'Moisturizer']

    plt.pie(eje_y, labels=etiquetas, autopct='%1.1f%%')

    plt.title('Sales data')
    plt.legend(loc='lower right', bbox_to_anchor=(1.3, 0))

    plt.show()

if __name__ == "__main__":
    ventas_anuales()