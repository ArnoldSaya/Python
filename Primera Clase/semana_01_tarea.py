# -*- coding: utf-8 -*-
"""Semana 01 - Tarea

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1K06Uf605zuQD1UboQk6SmGuRF0VXRgbZ

#Semana 01 - Tarea
"""

#José es administrador en una fábrica de chocolates, una de sus tareas es pedir las cajas al proveedor semanalmente, en cada caja entran 12 chocolates.
#Hacer un programa que le pida al jefe de producción la cantidad de chocolates que se producirán diariamente la próxima semana y resolver ¿qué debe hacer José?


total_chocolates = 0

for dia in range(1, 8):
    chocolates = int(input("Ingrese la cantidad de chocolates producidos en el día {}: ".format(dia)))
    total_chocolates += chocolates

cajas = total_chocolates // 12
sobrantes = total_chocolates % 12

print("José necesita {} cajas y sobrarán {} chocolates.".format(cajas, sobrantes))

#Dados los catetos de un triángulo rectángulo, calcular su hipotenusa

cateto1 = float(input("Ingrese la longitud del primer cateto: "))
cateto2 = float(input("Ingrese la longitud del segundo cateto: "))

hipotenusa = (cateto1**2 + cateto2**2)**0.5

print("La hipotenusa del triángulo es:", hipotenusa)

# Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
#Recordar que la fórmula para la conversión es: C = (F-32)*5/9

fahrenheit = float(input("Ingrese el valor en grados Fahrenheit: "))

celsius = (fahrenheit - 32) * 5 / 9


print("El equivalente en grados Celsius es:", celsius)

# Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor.

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

if num1 > num2:
    if num1 % num2 == 0:
        print(f"{num1} es múltiplo de {num2}.")
    else:
        print(f"{num1} no es múltiplo de {num2}.")
elif num2 > num1:
    if num2 % num1 == 0:
        print(f"{num2} es múltiplo de {num1}.")
    else:
        print(f"{num2} no es múltiplo de {num1}.")
else:
    print("Ambos números son iguales, por lo tanto son múltiplos entre sí.")

# Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor,
# asegurándose de que no se acepten números negativos ni cero.

num1 = int(input("Ingrese el primer número entero: "))
while num1 <= 0:
    print("El número debe ser positivo y mayor que cero.")
    num1 = int(input("Ingrese el primer número entero: "))

num2 = int(input("Ingrese el segundo número entero: "))
while num2 <= 0:
    print("El número debe ser positivo y mayor que cero.")
    num2 = int(input("Ingrese el segundo número entero: "))

if num1 > num2:
    if num1 % num2 == 0:
        print(f"{num1} es múltiplo de {num2}.")
    else:
        print(f"{num1} no es múltiplo de {num2}.")
elif num2 > num1:
    if num2 % num1 == 0:
        print(f"{num2} es múltiplo de {num1}.")
    else:
        print(f"{num2} no es múltiplo de {num1}.")
else:
    print("Ambos números son iguales, por lo tanto son múltiplos entre sí.")

# Escriba un programa que pida un año y que escriba si es bisiesto o no.

anio = int(input("Ingrese un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print(f"El año {anio} es bisiesto.")
else:
    print(f"El año {anio} no es bisiesto.")

# Muestra los múltiplos de 3 a partir del 3 hasta el número que el usuario indique.

numero = int(input("Ingrese un número: "))

print("Múltiplos de 3 hasta el número indicado:")
for i in range(3, numero + 1, 3):
    print(i)

# Escriba un programa que pida dos números enteros. El programa pedirá de nuevo el segundo número
# mientras no sea mayor que el primero. El programa terminará escribiendo los dos números.

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

while num2 <= num1:
    print("El segundo número debe ser mayor que el primero.")
    num2 = int(input("Ingrese el segundo número entero: "))

print(f"El primer número es: {num1} y el segundo número es: {num2}.")

# Escriba un programa que pida números enteros mientras sean cada vez más grandes.

numero = int(input("Ingrese un número entero: "))
while True:
    siguiente_numero = int(input("Ingrese el siguiente número entero: "))
    if siguiente_numero > numero:
        numero = siguiente_numero
    else:
        print("El número ingresado no es mayor que el anterior. El programa ha terminado.")
        break

# Escriba un programa que pida las notas de un grupo, se le preguntará al usuario si quiere seguir ingresando notas,
# y mientras la respuesta sea Sí/SÍ/sí, se debe seguir ingresando. Al finalizar el ingreso de notas,
# se debe mostrar una lista de las notas aprobadas y otra de las desaprobadas.

aprobadas = []
desaprobadas = []

while True:
    nota = float(input("Ingrese la nota del estudiante: "))

    if nota >= 11:
        aprobadas.append(nota)
    else:
        desaprobadas.append(nota)

    continuar = input("¿Desea ingresar otra nota? (Sí/SÍ/sí para continuar): ")
    if continuar.lower() != "sí":
        break

print("Notas aprobadas:", aprobadas)
print("Notas desaprobadas:", desaprobadas)

# Pedir el nombre de 5 asignaturas y su nota respectiva, luego mostrar los mensajes:
# “En la asignatura XXXXXXX sacó XXXXXX, para cada asignatura.”

asignaturas = []
notas = []

for i in range(5):
    asignatura = input(f"Ingrese el nombre de la asignatura {i+1}: ")
    nota = float(input(f"Ingrese la nota de {asignatura}: "))

    asignaturas.append(asignatura)
    notas.append(nota)

for i in range(5):
    print(f"En la asignatura {asignaturas[i]} sacó {notas[i]}.")

# Función para calcular el cargo del estacionamiento
def calcular_cargo(horas):
    if horas <= 1:
        return 3.00
    elif horas <= 23:
        return 3.00 + (horas - 1) * 0.50
    else:
        return 12.00  # Cargo máximo por día

# Pedir al usuario el número de horas
horas = float(input("Ingrese el número de horas estacionadas: "))
cargo = calcular_cargo(horas)

# Mostrar el cargo
print(f"El cargo por {horas} horas es: S/{cargo:.2f}")

# Función para determinar si el primero es múltiplo del segundo
def es_multiplo(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False

# Pedir al usuario los dos números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Verificar si es múltiplo
if es_multiplo(num1, num2):
    print(f"{num1} es múltiplo de {num2}.")
else:
    print(f"{num1} no es múltiplo de {num2}.")

# Función para convertir horas, minutos y segundos a segundos
def convertir_a_segundos(horas, minutos, segundos):
    return horas * 3600 + minutos * 60 + segundos

# Pedir al usuario las horas, minutos y segundos
horas = int(input("Ingrese el número de horas: "))
minutos = int(input("Ingrese el número de minutos: "))
segundos = int(input("Ingrese el número de segundos: "))

# Calcular el total en segundos
total_segundos = convertir_a_segundos(horas, minutos, segundos)

# Mostrar el resultado
print(f"El total en segundos es: {total_segundos} segundos.")