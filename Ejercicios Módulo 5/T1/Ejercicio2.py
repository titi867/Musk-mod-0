#Escribe una función para contar el número de líneas de un archivo de texto "historia.txt": 
# Ejemplo: Si el archivo "story.txt" contiene las siguientes líneas:
#Un niño está jugando allí.
#Hay un parque infantil.
#Un avión está en el cielo.
#El cielo es rosa.
#La contraseña puede tener letras y números.
#El resultado debe ser 5.

def contar_lineas():
    try:
        with open("historia.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            numero_de_lineas = len(lineas)
            print(f"Número total de líneas en 'historia.txt': {numero_de_lineas}")
    except FileNotFoundError:
        print("El archivo 'historia.txt' no se encontró.")

if __name__ == "__main__":
    contar_lineas()