def enteros(n):
    for i in range(n):
        yield i * 2

for numero in enteros(10):
    print("Número entero multiplicado por dos:", numero)