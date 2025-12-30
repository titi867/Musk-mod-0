def impares(n):
    for i in range(n):
        if i % 2 != 0:
            yield i

for numero in impares(10):
    print("Número impar:", numero)