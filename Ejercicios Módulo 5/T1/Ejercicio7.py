#Escribe un programa en Python para generar 26 archivos de texto llamados A.txt, B.txt, 
# y así sucesivamente hasta Z.txt.

def generar_archivos():
    for letra in range(ord('A'), ord('Z') + 1):
        nombre_archivo = f"{chr(letra)}.txt"
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write(f"{chr(letra)}.txt\n")
    print("Archivos generados exitosamente.")

if __name__ == "__main__":
    generar_archivos()