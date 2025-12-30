""" Crea una clase con el nombre de Estudiante e inicialice atributos como el
nombre, la edad y el grado mientras crea un objeto. """

class Estudiante:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    

estudiante_1 = Estudiante("Martín", 6, "1º Primaria")

print(f"Nombre: {estudiante_1.name}, Edad: {estudiante_1.age}, Grado: {estudiante_1.grade}")