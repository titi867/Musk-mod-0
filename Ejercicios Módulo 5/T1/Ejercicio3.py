#Escribe una función en Python para contar y mostrar el número total de palabras en un archivo de texto.

def contar_palabras():
    try:
        with open("poema.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            palabras = contenido.split()
            numero_de_palabras = len(palabras)
            print(f"El número total de palabras en el archivo es: {numero_de_palabras}")
    except FileNotFoundError:
        print("El archivo no existe.")

if __name__ == "__main__":
    contar_palabras()