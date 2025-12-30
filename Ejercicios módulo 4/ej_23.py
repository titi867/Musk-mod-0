class NegativeDifferenceException(Exception):
    def __init__(self, message="La diferencia es negativa"):
        self.message = message
        super().__init__(self.message)

def diferencia_entre_enteros(a, b):
    try:
        resultado = a - b
        if resultado < 0:
            raise NegativeDifferenceException()
        print("La diferencia entre", a, "y", b, "es:", resultado)
    except NegativeDifferenceException as e:
        print("Error:", e)

diferencia_entre_enteros(5, 10)