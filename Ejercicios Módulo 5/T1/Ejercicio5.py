#Escriba una función display_words() en Python para leer las líneas de un archivo de texto "story.txt", 
# y mostrar aquellas palabras que tengan menos de 4 caracteres.

def display_words():
    try:
        with open("story.txt", "r", encoding="utf-8") as file:
            for line in file:
                words = line.split()
                short_words = [word for word in words if len(word) < 4]
                for word in short_words:
                    print(word)
    except FileNotFoundError:
        print("El archivo story.txt no se encontró.")

if __name__ == "__main__":
    display_words()