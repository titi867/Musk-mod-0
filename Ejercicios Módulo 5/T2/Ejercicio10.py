#Combina dos dataframe utilizando la siguiente condición. Crea dos dataframe utilizando los siguientes 
# dos Dicts, fusiónalos y añade el segundo dataframe como una nueva columna al primer dataframe.
# Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925, 71400]}
# car Horsepower = {*Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182, 160]}

import pandas as pd

def merge_dataframes():
    
    car_price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925, 71400]}
    car_horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Horsepower': [141, 80, 182, 160]}
    
    df_price = pd.DataFrame(car_price)
    df_horsepower = pd.DataFrame(car_horsepower)
    
    merged_df = pd.merge(df_price, df_horsepower, on='Company')
    
    return merged_df

if __name__ == "__main__":
    print(merge_dataframes())