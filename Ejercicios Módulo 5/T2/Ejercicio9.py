#Concatena dos dataframes utilizando las siguientes condiciones:
# GermanCars = {
#     'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'],
#     'Price': [23845, 171995, 135925, 71400]
# }

# japaneseCars = {
#     'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi'],
#     'Price': [29995, 23600, 61500, 58900]
# }

import pandas as pd

def concatenar_dataframes():

    GermanCars = {
    'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'],
    'Price': [23845, 171995, 135925, 71400]
    }

    japaneseCars = {
        'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi'],
        'Price': [29995, 23600, 61500, 58900]
    }

    concatenados = pd.concat([pd.DataFrame(GermanCars), pd.DataFrame(japaneseCars)], keys = ["Alemania", "Japón"])
    return concatenados

if __name__ == "__main__":
    print(concatenar_dataframes())