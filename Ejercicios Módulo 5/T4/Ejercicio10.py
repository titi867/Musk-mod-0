# Lee todos los datos de las ventas de productos y
# muéstrelos mediante el diagrama de pila.

import pandas as pd
import matplotlib.pyplot as plt

def ventas_productos():

    datos = pd.read_csv('Modulo5_company_sales_data-221102-123259.csv')
    meses = datos['month_number']

    datos_ventas = [datos['facecream'],
                    datos['facewash'],
                    datos['toothpaste'],
                    datos['bathingsoap'],
                    datos['shampoo'],
                    datos['moisturizer']]

    etiquetas = ['Crema facial', 'Lavado de cara', 'Pasta de dientes',
                 'Gel de baño', 'Champú', 'Hidratante']
    
    colores = ['m', 'c', 'r', 'k', 'g', 'y']

    plt.stackplot(meses, datos_ventas, labels=etiquetas, colors=colores)

    plt.title("GitHub_MUSK: Todas las ventas de productos en un stack plot")
    plt.xlabel("Número de mes")
    plt.ylabel("Unidades de ventas en número")
    plt.legend(loc='upper left')

    plt.xticks(meses)
    plt.yticks(range(0, 35000, 5000))

    plt.show()


if __name__ == "__main__":
    ventas_productos()