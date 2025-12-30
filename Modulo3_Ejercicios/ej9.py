""" Añade un atributo de clase llamado escuela a la clase Estudiante
y dale un valor predeterminado. A continuación, añade un método
de clase que, dado el nombre de otra escuela, actualice el valor
de este atributo. Llama a tu método en el programa principal y 
asegúrate de que funciona """

class Estudiante:
    
    escuela = "Escuela por defecto"
    
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    @classmethod
    def CambiarEscuela(cls, nueva_escuela):
        cls.escuela = nueva_escuela
        return cls.escuela
    
estudiante_1 = Estudiante("Martín", 6, "1º Primaria")

Estudiante.CambiarEscuela("Escuela B")

print(f"El nueva escuela de {estudiante_1.name} es: {Estudiante.escuela}")

