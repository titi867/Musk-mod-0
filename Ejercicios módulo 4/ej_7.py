from datetime import datetime

def mostrar_fecha_hora():
    ahora = datetime.now()
    print("Fecha y hora actual:", ahora.strftime("%Y-%m-%d %H:%M:%S"))
    print("Año actual:", ahora.year)
    print("Mes actual:", ahora.month)
    print("Semana del año actual:", ahora.isocalendar()[1])
    print("Día de la semana actual:", ahora.strftime("%A"))
    print("Día del año actual:", ahora.timetuple().tm_yday)
    print("Día del mes actual:", ahora.day)

mostrar_fecha_hora()
