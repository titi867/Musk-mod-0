# 1. Haz un programa que escriba una línea con el mensaje “Buenos días a todo el mundo!”.

print("Buenos días a todo el mundo!")


# 2. Haz un programa que declare tres palabras a, b y c, y que escriba una línea con c, b y a en este orden.

a = "tijeras"
b = "papel"
c = "piedra"

print(c,b,a)


# 3. Haz un programa que declare dos números y que escriba la suma.

num1 = 85
num2 = 43

print(num1 + num2)


# 4. Haz un programa que declare dos números y que escriba el máximo.

num1 = 33
num2 = 42

print(max(num1,num2))


# 5. Haz un programa que declare tres números, todos diferentes, y que escriba el máximo.
num1 = 33
num2 = 47
num3 = 26

print(max(num1,num2,num3))


# 6. Hacer un programa que dado un valor calcule su cuadrado y el cubo. 

valor = 3

print(pow(valor,2))
print(pow(valor,3))


# 7. Haz un programa que devuelva el valor absoluto de un número.

num = -6.8

print(abs(num))



# 8. Haz un programa que lea dos naturales a y b, con b > 0, y que escriba la división entera d 
# y el residuo r de a entre b. Recordad que, por definición, d y r tienen que ser los únicos enteros 
# tales que 0 ≤ r < b y d · b + r = a. Ejemplo: a=32, b=5, d=6, r=2 ya que 32 = 5 * 6 + 2

a = 7
b = 4
d = int(a/b)
r = int(a%b)

print(d)
print(r)


# 9. Haz un programa que, dada una cantidad de segundos, diga cuántas horas, minutos y segundos representa.

segundos_totales = 3665
horas = segundos_totales // 3600
segundos_restantes = segundos_totales % 3600
minutos = segundos_restantes // 60
segundos_finales = segundos_restantes % 60

print(f"{horas}h,{minutos}m,{segundos_finales}s")

# 10. Haz un programa que dada una temperatura en grados Celsius la muestre en grados Fahrenheit 
# y en grados Kelvin. (F= 1.8C + 32 y  ºK =°C + 273ºK).

celsius = 37
fahrenheit = (1.8*celsius) + 32
kelvin = celsius + 273

print(f"{celsius} ºCelsius son {fahrenheit} ºFahrenheit y {kelvin} ºKelvin")

