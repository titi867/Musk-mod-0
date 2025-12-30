""" Añade un método privado en la clase anterior, que dado un diccionario
mes-número de asistencias, devuelva 1 si algún mes tiene una asistencia < 4,
devuelva 2 si algún mes tiene alguna asistencia entre [4,8] o bien devuelva 3
en caso contrario. Para probar el método privado, encapsúlalo con una función
pública que devuelva su resultado """

class Estudiante:
    escuela = "Escuela por defecto" 
    
    def __init__(self, name, age, grade, notas_iniciales={}):
        self.name = name
        self.age = age
        self.grade = grade
        self.notas = notas_iniciales
    
    def __verificar_asistencias(self, asistencias_mes):

        for mes, numero_asistencias in asistencias_mes.items():
            if numero_asistencias < 4:
                return 1
        
        for numero_asistencias in asistencias_mes.values():    
            if 4 <= numero_asistencias <= 8:
                return 2
                
        return 3
    
    def VerificarAsistencias(self, asistencias_mes):

        return self.__verificar_asistencias(asistencias_mes)

datos_asistencia = {
    "Enero": 10,
    "Febrero": 7,
    "Marzo": 3,
    "Abril": 9
}

estudiante_2 = Estudiante("Lucía", 10, "5º Primaria")

resultado_asistencia = estudiante_2.VerificarAsistencias(datos_asistencia)

print(f"Diccionario de asistencias: {datos_asistencia}")
print(f"El código de asistencia devuelto es: {resultado_asistencia}")