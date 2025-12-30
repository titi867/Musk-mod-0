""" Añade a la clase anterior un método estático que dada una
lista de notas y sus asignaturas asociadas como diccionario,
imprima aquellas asignaturas que han recibido una nota inferior a 5 """

class Estudiante:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def Media(self, grade):
        self.grade = sum(grade) / len(grade)
        return self.grade
    
    @staticmethod
    def NotasBajas(diccionario):
        for asignatura, grade in diccionario.items():
            if grade < 5:
                print(f"La nota de {asignatura} es: {grade}")    
    
diccionario_notas = {
    "Matemáticas": 6,
    "Lengua": 4,
    "Inglés": 8,
    "Historia": 3,
    "Ciencias": 7
}

Estudiante.NotasBajas(diccionario_notas)

