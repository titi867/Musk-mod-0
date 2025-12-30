from datetime import datetime

fecha_cadena = "Jan 1 2014 2:43PM"

fecha_convertida = datetime.strptime(fecha_cadena, "%b %d %Y %I:%M%p")

print(fecha_convertida.strftime("%Y-%m-%d %H:%M:%S"))