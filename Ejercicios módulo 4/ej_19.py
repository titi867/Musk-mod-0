def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

for numero in fibonacci(10):
    print("Número de Fibonacci:", numero)