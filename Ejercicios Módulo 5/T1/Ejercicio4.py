#Escriba una función en Python para leer líneas de un archivo de texto "notas.txt". 
# Su función debe encontrar y mostrar la aparición de la palabra "el".

def encontrar_palabra():
    with open("notas.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo:
            palabras = linea.split()
            for palabra in palabras:
                if palabra.lower() == "el":
                    print(palabra)

if __name__ == "__main__":
    encontrar_palabra()