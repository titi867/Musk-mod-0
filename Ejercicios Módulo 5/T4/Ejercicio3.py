# Lee todos los datos de ventas de productos y
# mostrarlos mediante un gráfico multilínea.
# Muestra el número de unidades vendidas por
# mes para cada producto utilizando gráficos
# multilínea. (es decir, una línea de trazado
# separada para cada producto).

import pandas as pd
import matplotlib.pyplot as plt

def graficar_ventas():

    datos = pd.read_csv('Modulo5_company_sales_data-221102-123259.csv')

    meses = datos['month_number']

    productos = {
            'facecream': {'label': 'Face Cream', 'color': 'blue'},
            'facewash': {'label': 'Face Wash', 'color': 'orange'},
            'toothpaste': {'label': 'Toothpaste', 'color': 'green'},
            'bathingsoap': {'label': 'Bathing Soap', 'color': 'red'},
            'shampoo': {'label': 'Shampoo', 'color': 'purple'},
            'moisturizer': {'label': 'Moisturizer', 'color': 'brown'}
        }


    for columna, info in productos.items():
        plt.plot(meses, datos[columna], marker='o', label=f"{info['label']} Sales Data", 
                 linewidth=3, color=info['color'])

    plt.title('Ventas')
    plt.xlabel('Número de mes')
    plt.ylabel('Unidades de ventas en número')

    plt.legend(loc='upper left')
    plt.xticks(meses)
    plt.yticks([1000, 2000, 4000, 6000, 8000, 10000, 12000, 15000, 18000])
    plt.show()

if __name__ == "__main__":
    graficar_ventas()

