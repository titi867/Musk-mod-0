#Escribe un programa en Python para añadir texto a un archivo y mostrar el texto en python.txt

def añadir_y_mostrar():
    texto_a_añadir = "Este es el texto nuevo que quiero añadir.\n"
    
    with open("python.txt", 'a', encoding='utf-8') as archivo:
        archivo.write(texto_a_añadir)
    
    with open("python.txt", 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()
        print("El contenido del archivo 'python.txt' es:")
        print(contenido)

if __name__ == "__main__":
    añadir_y_mostrar()