# Lee el beneficio total de cada mes y muéstralo utilizando 
# el histograma para ver los rangos de beneficio más comunes.

import pandas as pd
import matplotlib.pyplot as plt

def beneficio_mensual():

    datos = pd.read_csv('Modulo5_company_sales_data-221102-123259.csv')
    
    beneficio = datos['total_profit']
    
    rango_beneficio = [150000, 175000, 200000, 225000, 250000, 300000, 350000]
    
    plt.hist(beneficio, bins=rango_beneficio, label='Profit')
   
    plt.xlabel('Profit en dólares')
    plt.ylabel('Actual Profit en dólares')
    plt.title('Profit')
    
    plt.xticks(rango_beneficio)
    plt.yticks(range(0, 6, 1))
    plt.legend(loc='upper left')
    
    plt.show()

if __name__ == "__main__":
    beneficio_mensual()
