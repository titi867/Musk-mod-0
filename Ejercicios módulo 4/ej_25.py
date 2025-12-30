def division(a, b):
    try:
        resultado = a / b
        print(f"Resultado: {resultado}")
    except TypeError:
        print("Error: Los parámetros deben ser números enteros.")
    except ZeroDivisionError:
        print("Error: El divisor no puede ser 0.")
    finally:
        print("Cierre del programa.")


division(10, 2)
division(10, 0)
division(10, "hola")
