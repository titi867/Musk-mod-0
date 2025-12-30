#NO PUSE INPUTS EN ESTA TAREA



#CONDICIONALES
#1. Haz un programa que lea dos palabras y que indique el orden lexicográfico. 
# Escribe en una línea indicando si a < b, a > b o a = b. 
# Ejemplo: a = Anna, b = Javier, Anna < Javier.

a = "sandia"
b = "naranja"

if a < b:
    print (b)
if a > b:
    print (a)
if a == b:
    print("las dos palabras comienzan con la misma letra")


#2. Haz un programa que lea una letra y que indique por pantalla si es una mayúscula, 
# si es una minúscula, si es una vocal, y si es una consonante.

letra = "S"

if letra.isupper():
    print ("La letra es mayúscula")
else:
    print ("La letra es minúscula")

if (letra=="a" or letra=="e" or letra=="i" or letra=="o" or 
    letra=="u" or letra=="A" or letra=="E" or letra=="I" or 
    letra=="O" or letra=="U"):
    print ("La letra es vocal")
else:
    print("La letra es consonante")


#3. Haz un programa que lea un entero que representa una temperatura en grados Celsius, 
# y que diga si hace calor, si hace frío, o si se está bien. Suponed que hace calor si 
# la temperatura es más alta que 30 grados, que hace frío si es más baja que 10 grados, 
# y que se está bien en otro caso.

tempe = 25

if tempe <= 30 and tempe >= 10:  
    print("Se está bien")
elif tempe > 30:
    print("Hace calor")
elif tempe < 10:
    print("Hace frío")


#4. Haz un programa que, dados dos intervalos, calcule el intervalo correspondiente a la 
# intersección o indique que esta es vacía.

intervalo1 = [1, 8]
intervalo2 = [6, 12]

inicio_interseccion = max(intervalo1[0], intervalo2[0])
fin_interseccion = min(intervalo1[1], intervalo2[1])

if inicio_interseccion <= fin_interseccion:
    print(f"La intersección es [{inicio_interseccion}, {fin_interseccion}]")
else:
    print(f"No hay intersección")


#5. Haz un programa que indique si un año es bisiesto o no. Un año bisiesto tiene 366 días. 
# Después de la reforma gregoriana, los años bisiestos son los múltiplos de cuatro que no 
# acaban en dos ceros, y también los acabados en dos ceros tales que el número que queda 
# después de sacar los dos ceros finales es divisible por cuatro. Así, 1800 y 1900, 
# a pesar de ser múltiples de cuatro, no fueran bisiestos; en cambio, 2000 lo fue.

year = 1986

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"El año {year} es bisiesto")
else:
    print(f"El año {year} no es bisiesto")


#6. Haz un programa que añada un segundo en una hora del día, dadas sus horas, minutos y segundos.

hh = 23
mm = 59
ss = 00

ss = ss + 1

if ss >= 60:
    ss = 0
    mm = mm + 1

if mm >= 60:
    mm = 0
    hh = hh + 1

if hh >= 24:
    hh = 0

print(f"{hh:02}:{mm:02}:{ss:02}")
     

#7. Haz un programa que lea un real x≥0 y que escriba ⌊x⌋ (la parte entera inferior de x), 
# ⌈x⌉ (la parte entera superior de x), y el redondeo de x.

import math 

decimal = 7.52
floor = math.floor(decimal)
ceil = math.ceil(decimal)
rounded = round(decimal)

print(f"La parte entera inferior es {floor}")
print(f"La parte entera superior es {ceil}")
print(f"El número redondeado es {rounded}")



#BUCLES
#1. Haz un programa que lea dos números a y b, y que escriba todos los números enteros a y b. 
# Debe cumplirse que a < b. En caso que a > b, escribe los número de manera descendente.

a = 15
b = 8

if a < b:
    for num in range (a,b+1):
        print(num)
elif a > b:
    for num in range (a, b-1,-1):
        print(num)
else:
        print("Los números a y b son iguales")
    

#2. Haz un programa que lea una secuencia de 10 números y que escriba la media.

suma = 0
cantidad_num = 10

for i in range(cantidad_num):
    num = int(input(f"Ingresa el número {i + 1}: "))
    suma += num

media = suma / cantidad_num
print(f"La media de los {cantidad_num} números es: {media}")

# numeros = [9,5,6,8,3,7,15,2,80,44]
# suma = 0

# for numero in numeros:
#     suma += numero

# cantidad_numeros = len(numeros)

# if cantidad_numeros > 0:
#     media = suma / cantidad_numeros
#     print(media)
# else:
#     print("La lista está vacía")


#3. Haz un programa que dada una lista de naturales de tamaño n, indique la posición del primer número par.

posicion = 0
num_par = False

while not num_par:
    posicion += 1
    num = int(input(f"Ingresa el número en la posición {posicion}: "))

    if num % 2 == 0:
        print(f"El primer número par está en la posición: {posicion}")
        num_par = True
        break

# numeros = [3,5,6,9,2,3]
# encontrado = False 

# for i in enumerate(numeros):
#     if numeros[i]%2 == 0:
#         encontrado = True
#         print(f"El primer número está en la posición: {i}")
#         break

# if not encontrado:
#     print ("No hay ningún número para en la lista")


#4. Haz un programa que lea un número n y que escriba la “tabla de multiplicar” de n.

n = 9

for i in range (1,11):
    resultado = n * i
    print(f"{n} x {i} = {resultado}")


#5. Haz un programa que lea un número y que lo escriba del revés.

num = 357159
al_reves = 0

num_temporal = num

while num_temporal > 0:
    resultado = num_temporal % 10

    al_reves = (al_reves * 10) + resultado

    num_temporal = num_temporal // 10

print(f"El número {num} al revés es: {al_reves}")

# numero = 485692
# cadena = str(abs(numero))
# cadena_invertida = cadena[::-1]

# print(cadena_invertida)


#6. Haz un programa que lea un número y que escriba el número de dígitos.

num = 9513571234567893
contador = 0

num_temporal = abs(num)

if num_temporal == 0:
    contador = 1

else:
    while num_temporal > 0:
        num_temporal = num_temporal // 10
        contador += 1

print(f"El número {num} tiene {contador} dígitos")

# n = 9137842615167889
# digitos = len(str(abs(n)))

# print(digitos)


#7. Haz un programa que diga si un natural n es capicua o no.

num = 987357
num_temporal = num
al_reves = 0

while num_temporal > 0:
    resultado = num_temporal % 10
    al_reves = (al_reves * 10) + resultado
    num_temporal = num_temporal // 10

if num == al_reves:
    print(f"El número {num} es capicúa")

else:
    print(f"El número {num} no es capicúa")

# numero = 456654
# cadena = str(abs(numero))

# if cadena == cadena[::-1]:
#     print("Es capicúa")
# else:
#     print("No es capicúa")


#8. Haz un programa que dada una secuencia de años acabada en 0 nos diga cuántos hay del siglo 20.

contador = 0
año = int(input("Introduce un año (0 para terminar): "))

while año != 0:

    if 1901 <= año <= 2000:
        contador += 1
    año = int(input("Introduce un año (0 para terminar): "))

print(f"{contador} año(s) del siglo XX.")


#9. Haz un programa que reciba una secuencia de naturales de tamaño n y nos devuelva cuál es el 
# primer natural que tiene un valor inferior al primer natural leído.

referencia = int(input("Ingresa un número: "))
n = int(input("¿Cuántos números vas a ingresar?: "))

for i in range(n):
    numero = int(input("Escribe los números a continuación: "))
    if numero < referencia:
        print(f"El primer número menor que la referencia es: {numero}")
        break

else:
    print("No se ingresó ningún número menor que la referencia")



#10. Haz un programa que cuente cuántos valores hay en una secuencia de enteros acabada en 0.

contador = 0
numero = int(input("Ingresa un número (o 0 para terminar): "))

while numero != 0:
    contador += 1
    numero = int(input("Ingresa otro número (o 0 para terminar): "))

print (f"Se ingresaron {contador} números")




#11. Haz un programa que devuelva el máximo de una secuencia de temperaturas acabada en 1000.

temperatura = int(input("Ingresa una temperatura o 1000 para terminar: "))
max_temp = temperatura

while temperatura != 1000:
    if temperatura > max_temp:
        max_temp = temperatura
    temperatura = int(input("Ingresa otra temperatura o 1000 para terminar:"))

print(f"La temperatura máxima es: {max_temp}")


#12. Haz un programa que dada una secuencia de valores acabada en 0 compruebe que ningún valor supera 50.

numero = int(input("Ingresa un número o 0 para terminar: "))
mayor_que_50 = True

while numero != 0:
    if numero > 50:
        mayor_que_50 = False

    numero = int(input("Ingresa otro número o 0 para terminar: "))
    
if mayor_que_50:
    print("Ningún número de la secuencia es mayor que 50")
else:
    print("En la secuencia hay al menos un número mayor que 50")


#13. Haz un programa que dada una secuencia de valores acabada en 0 compruebe que ningún valor supera 50 
# y que no hay más de tres que superen 40.

count_mayor_40 = 0
hay_mayor_50 = False

numero = int(input("Ingresa un número o 0 para terminar: "))

while numero != 0:
    if numero > 50:
        hay_mayor_50 = True
    elif numero > 40:
        count_mayor_40 += 1
    numero = int(input("Ingresa otro número o 0 para terminar: "))

if hay_mayor_50:
    print("Hay al menos un número mayor que 50")
elif count_mayor_40 > 3:
    print("Hay más de 3 números mayores que 40")
else:
    print("La secuencia es válida: ningún número supera el 50 y no hay más de 3 mayores que 40")


#14. Haz un programa que dada una secuencia de valores acabada en 0 diga si hay más positivos o negativos.
# Definimos la secuencia de números.

x = [-8,4,-4,5,2,-6,0]

cont_pos= 0
cont_neg = 0


for numero in x:
    
    if numero == 0:
        break

    elif numero > 0:
        cont_pos += 1
    else:
        cont_neg += 1

if cont_pos > cont_neg:
    print("Hay más números positivos que negativos")
elif cont_pos == cont_neg:
    print("Hay igual cantidad de números positivos y negativos")
else:
    print("Hay más números negativos que positivos")



#15. Haz un programa que dada una secuencia de valores enteros acabada en 0 diga cuál es el número que
# hay antes de primer negativo encontrado.

#ME AYUDARON

x = int(input("Ingresa un número, positivo, negativo o 0 para terminar: "))

antes_negativo = None

while x != 0 :
    if x < 0:
        break

    y = int(input("Ingresa un número, positivo, negativo o 0 para terminar: "))
    antes_negativo = x
    x = y

if antes_negativo is not None:
    print(f"El número antes del primer negativo es: {antes_negativo}")
else:
    print("No se ingresó ningún número negativo.")


#16. Haz un programa que dada una secuencia de valores enteros acabada en 0 diga cuántos 
# son múltiples del primero.

primer_numero = int(input("Ingresa un número: "))
contador_multiplos = 0

x = int(input("Ingresa un número (0 para terminar): "))

while x != 0:
  if x % primer_numero == 0:
    contador_multiplos += 1
  x = int(input("Ingresa otro número (0 para terminar): "))


print(f"La cantidad de múltiplos del primer número es: {contador_multiplos}")


#17. Haz un programa que lea varias descripciones de rectángulos y de círculos, y que para 
# cada una escriba el área correspondiente. La entrada empieza con un número n, seguido de 
# n descripciones. Si es de un rectángulo, se tiene la palabra “rectángulo” seguida de dos 
# reales estrictamente positivos que indican la longitud y la anchura. Si es de un círculo, 
# se tiene la palabra “círculo” seguida de un real estrictamente positivo que indica el radio.

numero = int(input("Ingresa un número: "))

for i in range(numero):

    linea = input("Si es rectángulo, escribe 'rectángulo' y dame su longitud y su anchura. Si es círculo, escribe 'círculo' y su radio: ")
    partes = linea.split()
 

    if partes[0] == "círculo":
        radio = float(partes[1])
        area_circulo = 3.14 * (radio ** 2)
        print(f"Es un círculo. Su área es {area_circulo}")
    elif partes[0] == "rectángulo":
        longitud = float(partes[1])
        anchura = float(partes[2])
        area_rectangulo= longitud * anchura
        print(f"Es un rectángulo. Su área es {area_rectangulo}")   



#18. Haz un programa que lea un natural n, y que escriba el resultado de la suma siguiente: 
# 1^2 + 2^2 + … + (n−1)^2 + n^2 y el aspecto de la secuencia.

numero = int(input("Ingresa un número: "))
total = 0
secuencia = []

for i in range (1, numero+1):
    total += i**2
    secuencia.append(f"{i}^2")

texto_final = " + ".join(secuencia)

print(f"{texto_final} = {total}")


#EXTRAS
# 1. Usar un bucle y operaciones aritméticas para obtener el resultado de la suma de los dígitos de 98765

num = 98765
suma_digitos = 0
num_temporal = num

while num_temporal > 0:
    digito = num_temporal % 10
    suma_digitos += digito

    num_temporal = num_temporal // 10


print(f"La suma de los dígitos de {num} es: {suma_digitos}")


# 2. Usando un bucle, determina el primer dígito del número 745389 (sin convertir a texto).

num = 745389
num_temporal = num
primer_dígito = 0

while num_temporal >= 10:
    num_temporal = num_temporal // 10
    
primer_digito = num_temporal    

print(f"El primer número de {num} es {primer_digito}")


# 3. ¿Cuál es el resultado de la siguiente operación: (numero original) - (numero al revés)
# para el número 254? Resuelve el problema usando un bucle para invertir el número

num_original = 254
num_reves = 0

num_temporal = num_original

while num_temporal > 0:
    resultado = num_temporal % 10
    num_reves = (num_reves * 10) + resultado
    num_temporal = num_temporal // 10

resta = num_original - num_reves

print(resta)


# 4. Haz un programa que lea un número y que sume todos los dígitos, excepto el primero.

num = 745389
suma_sin_primero = 0

num_temporal = num

while num_temporal >= 10:
    num_temporal = num_temporal // 10

    primero = num_temporal

num_temporal = num

while num_temporal > 0:
    digito = num_temporal % 10

    suma_sin_primero += digito

    num_temporal = num_temporal // 10

    suma_final = suma_sin_primero - primero

    
print(f"La suma de todos los dígitos, excepto el primero, es: {suma_final}")


# 5. Haz un programa que lea un número y que indique si la suma de los dígitos
# pares es mayor que la suma de los dígitos impares.

num = 2543
suma_pares = 0
suma_impares = 0

num_temporal = num

while num_temporal > 0:

    digito = num_temporal % 10

    if digito % 2 == 0:
        suma_pares += digito
    else:
        suma_impares += digito

    num_temporal = num_temporal // 10

print(f"La suma de los números pares de {num} da como resultado: {suma_pares}")
print(f"La suma de los números pares de {num} da como resultado: {suma_impares}")

if suma_pares > suma_impares:
    print ("La suma de los números pares es mayor a la suma de los números impares")
else:
    print ("La suma de los números pares no es mayor a la suma de los números impares")

