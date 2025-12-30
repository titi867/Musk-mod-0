from datetime import date, timedelta

año = 2025

fecha = date(año, 1, 1)

while fecha.year == año:

    if fecha.weekday() == 6:
        print(fecha.strftime("%Y-%m-%d"))

    fecha += timedelta(days=1)
