from random import randint

def generar_numeros_aleatorios(n):
    for _ in range(n):
        yield randint(1, 100)

for numero in generar_numeros_aleatorios(10):
    print("Número aleatorio:", numero)