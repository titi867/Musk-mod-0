# 1.	Escribe un programa que imprima los números del 1 al 10 en una línea.

for num in range (0,10):
    print(num + 1,end= " ")

# 2.	Escribe un programa que imprima los números pares del 1 al 20.

for num in range (1,21):
    if num %2 == 0:
        print(num)
        num + 1

# 3.	Escribe un programa que calcule la suma de los primeros 10 números naturales.

suma = 0

for num in range (1,11):
    suma += num

print(suma)

# 4.	Escribe un programa que imprima la tabla de multiplicar del 5.

multiplo = 5

for num in range (1,11):

    resultado = num * multiplo
    print(f"{num} x {multiplo} = {resultado}") 

# 5.	Escribe un programa que imprima los caracteres de una cadena de texto uno por uno.

cadena = "Hola, me gusta la IA"

for letra in cadena:
    print(letra)

# 6.	Escribe un programa que calcule el factorial de un número ingresado por el usuario.

numero_ingresado = 8
factorial = 1

for num in range (1,numero_ingresado + 1):
    factorial = factorial * numero_ingresado

print(f"El resultado del factorial de {numero_ingresado} es: {factorial}")

# 7.	Escribe un programa que calcule e imprima la suma de los números pares del 1 al 100.

suma_pares = 0

for num in range(0,101):
    if num % 2 == 0:
        suma_pares += num

print (suma_pares)        

# 8.	Escribe un programa que imprima la serie de Fibonacci hasta el décimo término.

inicio_serie = 0
fin_serie = 1

print(inicio_serie, end=", ")
print(fin_serie, end="")

for _ in range (8):
    numero_secuencia = inicio_serie + fin_serie
    print(f", {numero_secuencia}", end = " ")
    inicio_serie = fin_serie
    fin_serie = numero_secuencia


# 9.	Escribe un programa que imprima los números del 1 al 100, pero que reemplace los 
# múltiplos de 3 por "Fizz", los múltiplos de 5 por "Buzz" y los múltiplos de ambos por "FizzBuzz".

for num in range (1,101):
    if num % 3 == 0 and num %5 == 0:
        print ("FizzBuzz")
    elif num % 3 == 0:
        print ("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)


# 10.	Escribe un programa que encuentre e imprima todos los números primos menores que 100.

for numero in range (2, 100):
    es_primo = True

    for divisor in range(2, int(numero**0.5) + 1):
        if numero % divisor == 0:
            es_primo = False
            break
    if es_primo:
        print(numero,end= " ")


#EXTRA CHATGPT: Escribe un programa que imprima los números pares del 2 al 20, y al lado de cada uno, su cuadrado.

for numero in range(2, 20):
    cuadrado = numero**2
    es_par = False

    for cadena_pares in range(1,int(numero) + 1):
        if numero%2==0:
            es_par = True
            break
    if es_par:
        print(numero,cuadrado, end= " ")


#EXTRA CHATGPT: Haz un programa que imprima una cuenta regresiva del 10 al 1 (ambos incluidos) y 
# esperando 1 segundo en imprimir cada número, seguida de un 🚀

import time

for conteo in range (10,0,-1):

    print(conteo,"\n")
    time.sleep(1)

print("🚀")

#EJERCICIOS EXTRA: COMPRENSIÓN DE LISTAS:

# 1. Crea una lista con los cuadrados de los números del 1 al 10, usando comprensión de listas.
# 2. Tienes una lista de palabras y quieres quedarte sólo con las que tienen más de 5 letras.
# 3. Dado un string, cre auna lista con sólo las letras mayúsculas.
# 4. Crea una tupla con los números pares entre 1 y 20.
# 5. Dado un string, crea una lista con todas las letras únicas (sin repetir).