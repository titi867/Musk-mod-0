def excepciones():
    try:
        numero = int(input("Ingrese un número entero: "))
        resultado = 10 / numero
        print("El resultado de 10 dividido por", numero, "es:", resultado)

    except Exception as e:
        print("Se ha producido una excepción:")
        print("Tipo de error:", type(e).__name__)
        print("Argumentos:", e.args)
        print("Mensaje:", e)

excepciones()