from datetime import datetime, timedelta

hora_actual = datetime.now()

hora_modificada = hora_actual + timedelta(seconds=5)

print("Hora actual:", hora_actual.strftime("%H:%M:%S"))
print("Hora más 5 segundos:", hora_modificada.strftime("%H:%M:%S"))   