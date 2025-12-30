#STRINGS

#1. Haz un programa que lea una secuencia de caracteres acabada en punto y que escriba cuántas letras 'a' contiene.

caracteres = str(input("Escribe una cadena que finalice en un punto."))
contador = 0

for caracter in caracteres:

    if caracter == "a":
        contador += 1

print(f"La cadena tiene un total de {contador} letras 'a'")
    

#2. Haz un programa que encuentre todas las apariciones de una subcadena en una cadena dada.

cadena = "Hoy hace muchísimo calor en Murcia, pero no hace calor en Santiago"
subcadena = "calor en"

posiciones = []
inicio = 0

while True:
    index = cadena.find(subcadena, inicio)
    if index == -1:
        break
    posiciones.append(index)
    inicio = index + 1

print(f"La subcadena {subcadena} aparece en las posiciones: {posiciones}")

#3. Haz un programa que invierta una cadena.

cadena = "Justina Araneda Rodríguez"
cadena_invertida = cadena[::-1]

print(cadena_invertida)

#4. Haz un programa que divida una cadena en guiones.

cadena = "Hola mundo"
con_guiones = "-".join(cadena)

print(con_guiones)

#5. Haz un programa que añada una nueva cadena en medio de una cadena dada.

cadena = "Hola mundo"
nueva = "cruel"

palabras = cadena.split()
mitad = len(palabras) // 2

palabras_final = palabras[:mitad] + nueva.split() + palabras[mitad:]

resultado = " ".join(palabras_final)

print(resultado)
    
#6. Haz un programa que encuentre la última posición de una subcadena dada.

cadena = "Hoy hace muchísimo calor en Murcia, pero no hace calor en Santiago"
subcadena = "calor en"

ultima_subcadena = cadena.rfind(subcadena)

if ultima_subcadena != -1:
    print(f"La última posición de {subcadena} está en la posición {ultima_subcadena}")
else:
    print("No se encuentra la subcadena")

#7. Haz un programa que elimine cadenas vacías de una lista de cadenas.

lista = ["Hola", " ", "", "Mundo", "de", " ", "","Python"]

elimina = [cadena for cadena in lista if cadena.strip() != ""]

print(elimina)

#8. Haz un programa que elimine símbolos especiales / signos de puntuación de una cadena.

import string

cadena = "Hola Mundo! Vamos a programar? :) Qué alegría! <#"
elimina = "".join([c for c in cadena if c not in string.punctuation])

print(elimina)

#9. Haz un programa que encuentre palabras con letras y números.

import re

cadena = "Los usuarios existentes son Hola123, Pr0gr4mm3r y 420"

palabras = cadena.split()
letras_numeros = [p for p in palabras if re.search(r'[a-aZ-Z]', p) and re.search(r'[0-9]', p)]

print(f"Las palabras con letras y números son: {letras_numeros}")

#10. Haz un programa que sustituya cada símbolo especial por # en la siguiente cadena.

import string

cadena = "Hola Mundo! Vamos a programar? :) Qué alegría! <Python>"
sustituye = "".join([c if c not in string.punctuation else "#" for c in cadena])

print(sustituye)

#LISTAS

#1. Haz un programa que lea una lista dado su tamaño e imprima el segundo elemento (si existe).

colores = ["azul", "rojo", "amarillo", "verde", "morado"]
elemento = colores[2]

if elemento in colores:
    print(elemento)
else:
    print("No hay elementos en la segunda posición")

#2. Haz un programa que lea una secuencia no vacía de enteros acabada en -1 y que escriba cuántos son iguales al último.
#NO SE REFIERE A QUE EL '-1' SEA EL ÚLTIMO ELEMENTO DE LA SECUENCIA, ES COMO SI EL MENOS UNO FUERA IGUAL A "FIN",
#ASÍ QUE EL ÚLTIMO NÚMERO DE ESTA LISTA ES EL 14

numeros = [1, 7, 14, 6, 3, -14, 8, 14, -1]
contador = 0

for numero in numeros:
    if numero == numeros[-2]:
        contador+=1

print(f"La cantidad de números iguales a {numeros[-2]} es {contador}")

#3. Haz un programa que lea secuencias de enteros acabada en -1 y que escriba cada una invirtiendo el orden de sus elementos.

numeros = [1, 7, 14, 6, 3, -14, 8, 14, -1]

print(numeros[::-1])

#4. Haz un programa que lea n palabras y que escriba cada una invirtiendo el orden de sus caracteres.

lista = ["canción", "silla", "auto", "botella", "libro", "juguete"]

lista_invertida = []

for palabra in lista:

    lista_invertida.append(palabra[::-1])

print(lista_invertida)

#5. Haz un programa que lea una secuencia de números mientras sean positivos y que escriba la media.

secuencia = [7, 5, -8, 2, 15, -1, 63, -46, 3]
contador = 0
suma = 0

for numero in secuencia:
    if numero > 0:
        contador += 1
        suma += numero

if contador == 0:
    print("No hay números positivos")
else:
    media = suma/contador
    print(f"La media es: {media:.2f}")

#6. Haz un programa que devuelva la concatenación de v1 y v2 son dos listas de tamaño n y m, es decir, hay que devolver 
# un vector que tenga los elementos de v1 seguidos de los elementos v2.

v1 = [1, 2, 3]
v2 = [4, 5, 6, 7, 8, 9, 10]

v1.extend(v2)

print(f"La unión de ambas listas es: {v1}")

#7. Haz un programa que almacene en una lista los siguientes precios: 50, 75, 46, 22, 80, 65, 8 y muestre por pantalla el 
# menor y el mayor de los precios.

precios = [50, 75, 46, 22, 80, 65, 8]

print(f"El menor precio de la lista es: {min(precios)} y el precio mayor es: {max(precios)}")

#8. Haz un programa que almacene las asignaturas de un curso (por ejemplo, Matemáticas, Física, Química, Historia y Lengua) 
# en una lista y muestre por pantalla.

asignaturas = "Matemáticas", "Física", "Química", "Historia", "Lengua"

print(f"Las asignaturas son:", ", ".join(asignaturas))

#9. Haz un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.

lista = []

for lista in range(10, 0, -1):
    print(lista)

#10. Haz un programa que concatene dos listas del mismo tamaño n alternando elementos de una lista y otra.

lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]

nueva_lista = []

for a, b in zip(lista_1, lista_2):
    nueva_lista.extend([a, b])

print(f"La nueva lista es: {nueva_lista}")

#11. Haz un programa que itere ambas listas de tamaños n y m (siendo n y m números distintos) simultáneamente e imprima sus elementos.

from itertools import zip_longest 

lista_1 = ["alegría", "emoción", "ilusión"]
lista_2 = ["enfado", "tristeza"]

for a, b in zip_longest(lista_1, lista_2, fillvalue="-"):
    print(a, b)

#12. Haz un programa que añada un nuevo elemento 60 a la lista [10, 50, 40, 20, 30] después de un elemento especificado por el usuario.
# Si el elemento introducido no está presente en la lista, debe mostrar el mensaje: "Elemento no presente en la lista".

lista = [10, 50, 40, 20, 30]

numero = int(input(f"Qué número quieres: {lista}"))

if numero in lista:
    posicion = lista.index(numero)
    lista.insert(posicion + 1, 60)
    print(f"La lista final es: {lista}")
else:
    print("Elemento no presente en la lista")

#13. Haz un programa que elimine todas las apariciones de un elemento específico introducido por el usuario de la lista [10, 50, 40, 20, 60, 30].

lista = [10, 50, 40, 20, 60, 30]

quitar = int(input("Qué número quieres quitar?"))

if quitar in lista:
    lista = [x for x in lista if x!= quitar] #COMPRENSIÓN DE LISTAS: forma compacta de escribir un bucle con una condición.
    # nueva_lista = []
    # for x in lista:
    #     if x != quitar:
    #         nueva_lista.append(x)
    #     lista = nueva_lista // FORMA LARGA
    print(f"La lista final es: {lista}")
else:
    print("Elemento no presente en la lista")


#TUPLAS

#1. Haz un programa que invierta una tupla.

tupla = (2, 7, 5, 8, 1)

print(tupla[::-1])

#2. Haz un programa que acceda al valor 15 de la tupla.

tupla = (2, 3 ,4, 6, 7, 4, 1, 6, 13, 0, 5, 7, 25, 12, 2, 1)

tupla = list(tupla)

if 15 in tupla:
    print("El número 15 está en la tupla")
else:
    print("El número 15 no está en la tupla")

#3. Haz un programa que declare una tupla con un solo elemento 10.

tupla = (10,)

print(tupla)

#4. Haz un programa que descomponga una tupla en 4 variables.

tupla = (4, 5, 6, 7)
a, b, c, d = (4, 5, 6, 7)

print(a, b)
print(c, d)

#5. Haz un programa que intercambie dos tuplas en Python.

tupla_1 = (4, 8, 12)
tupla_2 = (1, 7, 2)

tupla_1, tupla_2 = tupla_2, tupla_1

print(f"La nueva tupla_1 es: {tupla_1}")
print(f"La nueva tupla_2 es: {tupla_2}")

#6. Haz un programa que copie elementos específicos de una tupla a una nueva tupla.

tupla = (2, 4, 9, 1, 4, 6)

nueva_tupla = tuple(x for x in tupla if x == 9 or x == 4)

print(nueva_tupla)

#7. Haz un programa que modifique una tupla.

tupla = (2, 6, 4, 8, 12, 3, 9)
tupla = list(tupla)

tupla[4] = 7

tupla = tuple(tupla)

print(tupla)

#8. Ordena una tupla de tuplas por el 2º elemento.

#NO APARECE EN LAS CLASES, SEGÚN LO QUE HE INVESTIGADO HAY QUE USAR LAMBDA, PERO NO SÉ HACERLO BIEN...

#9. Haz un programa que cuente el número de apariciones del elemento 50 de una tupla.

tupla = (10, 50, 40, 20, 50, 30)

print(f"El número 50 aparece: {tupla.count(50)} veces")

#10. Haz un programa que compruebe si todos los elementos de la tupla son iguales.
    
tupla = (3, 2, 4, 3)

iguales = True

for x in tupla:
    if x != tupla[0]:
        iguales = False
        break
print(iguales)

#print(len(set(tupla)) == 1) // OTRA FORMA, TB DA UN BOOLEANO

#print(all(x == tupla[0] for x in tupla)) // ALTERNATIVA MÁS COMPACTA


#DICCIONARIOS

#1. Haz un proograma que convierta dos listas en un diccionario.

lista_1 = ["nombre", "raza"]
lista_2 = ["Mijo", "labrador negro"]

diccionario = dict(zip(lista_1, lista_2))

print(diccionario)

#2. Haz un programa que fusione dos diccionarios de Python en uno solo.

diccionario_1 = {"nombre": "Mijo", "raza": "labrador negro"}
diccionario_2 = {"dueño" : "Rubén", "edad": "33"}
fusion = {**diccionario_1, **diccionario_2}
print(fusion)

#3. Haz un programa que imprima el valor de la clave "history" del siguiente diccionario:
"""
Input:

{
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
    
Output: 80 """

diccionario = {"class": {"student": {"name": "Mike", "marks": {"physics": 70,"history": 80}}}}

history = diccionario["class"]["student"]["marks"]["history"]

print(history)

#4. Haz un programa que inicialice el diccionario por defecto.

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

diccionario = dict.fromkeys(employees, defaults)

print(diccionario)


#5. Haz un programa que cree un diccionario extrayendo las claves de un diccionario dado.    

sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}

keys = ["name", "salary"]

diccionario = {k: sample_dict[k] for k in keys}

print(diccionario)

#6. Haz un programa que elimine una lista de claves de un diccionario.

sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
keys = ["name", "salary"]

for x in keys: sample_dict.pop(x)

print(sample_dict)

#7. Haz un programa que compruebe si un valor existe en un diccionario.

diccionario = {"nombre": "Mijo", "raza": "labrador negro", "dueño" : "Rubén", "edad": "33"}

print("Rubén" in diccionario.values())

#8. Haz un programa que cambie el nombre de la clave de un diccionario.

diccionario = {"nombre": "Mijo", "raza": "labrador negro", "dueño" : "Rubén", "edad": "33"}

diccionario["nombre del dueño"] = diccionario.pop("dueño")

print(diccionario)

#9. Haz un programa que obtenga la clase de un valor mínimo del siguiente diccionario.

sample_dict = {"name": "Kelly","age": 25, "salary": 8000, "city": "New york"}

solo_numeros = {k: v for k, v in  sample_dict.items() if isinstance(v, (int, float))}

clave_min = min(solo_numeros, key=solo_numeros.get)

print(clave_min)

#10. Haz un programa que cambie el valor de una clave en un diccionario anidado.

mascotas = {"animal": {"perro": {"nombre": "Mijo", "raza": "labrador negro", "dueño" : "Ruben"},}}

raza = mascotas["animal"]["perro"]["raza"] = "labrador"

print(raza)


#SETS

#1. Haz un programa que añada una lista de elementos a un conjunto.

conjunto = {"Manzana", "Naranja", "Sandía"}

lista = ["Melocotón", "Cerezas"]

conjunto.update(lista)

print(conjunto)

#2. Haz un programa que devuelva un nuevo conjunto de elementos idénticos de dos conjuntos.

conjunto_1 = {"Amarillo", "Verde", "Rojo", "Rosa", "Azul"}
conjunto_2 = {"Rojo", "Negro", "Verde", "Naranja", "Celeste"}

nuevo_conjunto = conjunto_1.intersection(conjunto_2)

print(nuevo_conjunto)

#3. Haz un programa que obtenga sólo elementos únicos de dos conjuntos. (igual al 2)

conjunto_1 = {"Amarillo", "Verde", "Rojo", "Rosa", "Azul"}
conjunto_2 = {"Rojo", "Negro", "Verde", "Naranja", "Celeste"}

print(conjunto_1 & conjunto_2)

#4. Haz un programa que actualice el primer conjunto con elementos que no existen en el segundo conjunto.

conjunto_1 = {"Amarillo", "Verde", "Rojo", "Rosa", "Azul"}
conjunto_2 = {"Rojo", "Negro", "Verde", "Naranja", "Celeste"}

conjunto_1.difference_update(conjunto_2)

print(conjunto_1)

#5. Haz un programa que elimine elementos del conjunto a la vez.

conjunto = {"Amarillo", "Verde", "Rojo", "Rosa", "Azul"}

items_eliminar = {"Amarillo", "Rojo"}

print(conjunto - items_eliminar)


#6. Haz un programa que devuelva un conjunto de elementos presentes en el conjunto A o B, pero no en ambos.

conjunto_1 = {"Amarillo", "Verde", "Rojo", "Rosa", "Azul"}
conjunto_2 = {"Rojo", "Negro", "Verde", "Naranja", "Celeste"}

nuevo_conjunto = conjunto_1.symmetric_difference(conjunto_2)

print(nuevo_conjunto)


#7. Haz un programa que compruebe si dos conjuntos tienen algún elemento en común. En caso afirmativo, 
# mostrar los elementos comunes.

conjunto_1 = {"Amarillo", "Verde", "Rojo", "Rosa", "Azul"}
conjunto_2 = {"Rojo", "Negro", "Verde", "Naranja", "Celeste"}

if not conjunto_1.isdisjoint(conjunto_2):
    print("Los conjuntos tienen elementos en común")

    comunes = conjunto_1.intersection(conjunto_2)
    print(f"Elementos comunes: {comunes}")
else:
    print("Los conjuntos no tienen elementos en común")


#8. Haz un programa que actualice el conjunto1 añadiendo elementos del conjunto2, excepto los elementos comunes.

conjunto_1 = {"Amarillo", "Verde", "Rojo", "Rosa", "Azul"}
conjunto_2 = {"Rojo", "Negro", "Verde", "Naranja", "Celeste"}

conjunto_1.symmetric_difference_update(conjunto_2)

print(conjunto_1)

#9. Haz un programa que actualice el conjunto1 añadiendo elementos del conjunto 2, excepto los elementos comunes. (igual al 8)

conjunto_1 = {"Amarillo", "Verde", "Rojo", "Rosa", "Azul"}
conjunto_2 = {"Rojo", "Negro", "Verde", "Naranja", "Celeste"}

conjunto_1.symmetric_difference_update(conjunto_2)

print(conjunto_1)