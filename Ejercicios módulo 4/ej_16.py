from datetime import date, timedelta

fecha_inicial = date(2023, 1, 1)

for i in range(12):
    nueva_fecha = fecha_inicial + timedelta(days=20 * i)
    
    print(nueva_fecha)