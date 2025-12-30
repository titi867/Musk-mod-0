from datetime import date

contador = 0

for año in range(2015, 2017):
    for mes in range(1, 13):
        primer_dia = date(año, mes, 1)
        if primer_dia.weekday() == 0:
            contador += 1
            print(primer_dia.strftime("%B %Y")) #mes y año

print("Total de meses que comienzan en lunes entre 2015 y 2016:", contador)
        