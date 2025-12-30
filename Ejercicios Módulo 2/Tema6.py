# 1.Haz un programa que cree una función en Python que, dada una secuencia,
# devuelva únicamente los números pares.

def filtrar_pares(secuencia):
    par = []

    for numero in secuencia:
        if numero % 2 == 0:
            par.append(numero)
    return par


lista = [1, 5, 9, 7, 5, 3, 4, 2, 6, 8]
pares = filtrar_pares(lista)

print(pares)


# 2. Haz un programa que cree una función con longitud variable de argumentos.

def longitud(*args):
    return len(args)

print(longitud(10, 20, 30, 40))

# 3. Haz un pograma que devuelva múltiples valores desde una función. Crea la
# función calculation(), de modo que pueda aceptar dos variables y calcular
# sumas y restas. Además, debe devolver tanto la suma como la resta en una sola llamada.

def calculation(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

resultado_suma, resultado_resta = calculation(10, 5)

print(f"Suma: {resultado_suma}. Resta: {resultado_resta}")

# 4.Haz un programa que cree una función con un argumento por defecto. Crea una
# función show_employee() usando las siguientes condiciones:
# - Debe aceptar el nombre y el salario del empleado y mostrar ambos.
# - Si falta el salario en la llamada de la función, asigne el  valor
# predeterminado 9000 al salaio. 

# Input:
    
# showEmployee("Ben", 12000)
# showEmployee("Jessa")

# Output:

# Name: Ben salary: 12000
# Name: Jessa salary: 9000
    
def show_employee(nombre, salario = 9000):
    print(f"Name: {nombre}, Salary: {salario}")

show_employee("Ben", 12000)
show_employee("Jessa")


# 5. Haz un programa que cree una función interna para calcular la suma de
# la siguiente manera: Crea una función externa que acepte dos parámetros, a y b.
# Crea una función interna dentro de una función externa que calculará la suma de
# a y b. Por último, una función externa que sumará 5 en la suma y la devolverá.

def externa(a, b):
    def interna(x, y):
        return x + y
    suma = interna(a, b)
    return suma + 5

print(externa(3, 2))

# 6. Haz un programa que cree una función que escriba el cuadrado y la raíz de una
# secuencia de naturales.

import math

def cuadrado_raiz(secuencia):
    for numero in secuencia:
        print(f"Numero: {numero}, Cuadrado: {numero**2}, Raíz: {math.sqrt(numero)}")

print(cuadrado_raiz([1, 4, 9, 16, 25]))

# 7. Haz un programa que cree una función que deje a, b y c ordenados de pequeño a
# grande. Por ejemplo, si a=7, b=-3 y c=1, los valores después de la llamada deben
# ser a=-3, b=1 y c=7

def menor_a_mayor(a, b, c):
    lista = [a, b, c]
    lista.sort()
    return lista[0], lista[1], lista[2]

a, b, c = menor_a_mayor(7, -3, 1)

print(f"a: {a}, b: {b}, c: {c}")