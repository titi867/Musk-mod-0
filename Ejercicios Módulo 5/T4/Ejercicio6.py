# Lee los datos de ventas de jabón de baño de todos los 
# meses y muéstralos mediante un gráfico de barras.
# Guarda este gráfico en tu disco duro.

import pandas as pd
import matplotlib.pyplot as plt

def ventas_jabon():

    datos = pd.read_csv('Modulo5_company_sales_data-221102-123259.csv')
    
    meses = datos['month_number']
    jabon = datos['bathingsoap']

    plt.bar(meses, jabon, width=0.6)
    plt.xlabel('Número del mes')
    plt.ylabel('Unidades de ventas en número')
    plt.title('Ventas de jabón de baño')

    plt.xticks(meses)
    plt.yticks(range(0, 14000, 2000))
    plt.grid(linestyle='--', alpha=0.5)
    plt.savefig('ventas_jabon_bano.png')
    plt.show()

if __name__ == "__main__":
    ventas_jabon()