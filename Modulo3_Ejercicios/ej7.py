""" Añade un método público en la clase Estudiante que calcule la media 
de una lista de notas y actualice el valor del atributo grade. A
continuación llama a la función en tu programa principal e imprime
el valor de grade """

class Estudiante:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def Media(self, notas):
        self.grade = sum(notas) / len(notas)
        return self.grade
    
notas = [7, 8, 6, 9, 5]
estudiante_1 = Estudiante("Martín", 6, "1º Primaria")

print(f"La media de {estudiante_1.name} es: {estudiante_1.Media(notas)}")