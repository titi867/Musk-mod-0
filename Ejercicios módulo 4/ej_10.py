from datetime import datetime, timedelta

fecha_actual = datetime.now()

fecha_modificada = fecha_actual - timedelta(days=5)

print("Fecha actual:", fecha_actual.strftime("%Y-%m-%d"))
print("Fecha menos 5 días:", fecha_modificada.strftime("%Y-%m-%d"))
