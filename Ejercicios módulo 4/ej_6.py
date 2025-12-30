class Algoritmo:
    def __init__(self, nombre, tarea, aprendizaje):
        self.nombre = nombre
        self.tarea = tarea
        self.aprendizaje = aprendizaje
    
class BaseClassifier(Algoritmo):
    def __init__(self, nombre, tarea, aprendizaje):
        super().__init__(nombre, tarea, aprendizaje)
        

print(issubclass(BaseClassifier, Algoritmo))  # True
print(issubclass(Algoritmo, BaseClassifier))  # False

modelo = BaseClassifier("SVM", "Clasificación", "Supervisado")

print(isinstance(modelo, BaseClassifier))  # True
print(isinstance(modelo, Algoritmo))        # True

