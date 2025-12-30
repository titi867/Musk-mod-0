#1. Haz un programa que lea un número decimal por pantalla, 
# lo convierta a entero y lo imprima.

decimal = float(input("Escribe un número decimal: "))
entero =int(decimal)

print(entero)


#2. Haz un programa que lea un número decimal por pantalla 
# e imprima su tipo y su valor redondeado en la misma línea.

decimal = float(input("Escribe un número decimal con más de 2 decimales: "))
redondeado = round(decimal, 2)

print(type(decimal), redondeado)



#3. Haz un programa que lea dos números por pantalla e imprima 
# su diferencia en valor absoluto.

num1 = int(input("Diga un número: "))
num2 = int(input("Diga otro número: "))
resta = num1 - num2

print(abs(resta))

