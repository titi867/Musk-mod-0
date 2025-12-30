# Escribe una función en python para leer el contenido de un archivo de texto "poema.txt"
# línea por línea y mostrar el mismo en pantalla.

def leer_poema():
    try:
        with open("poema.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                print(linea.strip())
    except FileNotFoundError:
        print("El archivo 'poema.txt' no se encontró.")


if __name__ == "__main__":
    leer_poema()