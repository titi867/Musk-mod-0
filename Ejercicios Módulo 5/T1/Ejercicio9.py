#Escribe un programa en python para calcular la frecuencia de todas las palabras de un archivo txt.

def frecuencia_palabras():
    frecuencia = {}
    try:
        with open("poema.txt", 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                palabras = linea.split()
                for palabra in palabras:
                    palabra = palabra.lower().strip('.,¡!?;"()[]')
                    if palabra in frecuencia:
                        frecuencia[palabra] += 1
                    else:
                        frecuencia[palabra] = 1
        return frecuencia
    except FileNotFoundError:
        print("El archivo 'poema.txt' no se encontró.")
        return None

if __name__ == "__main__":
    resultado = frecuencia_palabras()
    if resultado:
        print("Frecuencia de palabras:")
        print("")
        for palabra, cantidad in resultado.items():
            print(f"{palabra}: {cantidad}")