from datetime import datetime

timestamp_str = "1284105682"

timestamp = int(timestamp_str)

fecha_legible = datetime.fromtimestamp(timestamp)

print("Fecha legible:", fecha_legible.strftime("%Y-%m-%d %H:%M:%S"))
