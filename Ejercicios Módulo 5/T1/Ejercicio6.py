#Un archivo de texto llamado "materia.txt" contiene algún texto que necesita ser mostrado de manera 
# que cada carácter siguiente esté separado por un símbolo "#". Escriba una definción de función para 
# hash_display() en Python que muestre todo el contenido del archivo matter.txt en el formato deseado. 
# Ejemplo: Si el archivo materia.txt tiene el siguiente contenido almacenado:
#EL MUNDO ES REDONDO
#La función hash_display() debe mostrar el siguiente resultado:
#E#L# #M#U#N#D#O# #E#S# #R#E#D#O#N#D#O

def hash_display():
    try:
        with open("materia.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            resultado = "#".join(contenido)
            print(resultado)
    except FileNotFoundError:
        print("El archivo 'materia.txt' no se encontró.")

if __name__ == "__main__":
    hash_display()

