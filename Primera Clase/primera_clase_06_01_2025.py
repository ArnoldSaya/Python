# -*- coding: utf-8 -*-
"""Primera clase 06/01/2025.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-81Chr_18ATvdkhLcPP56jlb1uQQqIr9

#Primera clase
##Variable
Una variable 3 cosas importantes
Tipo de dato
Nombre del identicador: No puede tener espacios en la variable, No puede empezar con un numero, No puede ser una palabra reservada.
Valor Almacenado

Variable normal: minusculas
Variable constante: MAYUSCULAS

##Tipo de variable

None: no tiene valor y se le asignara despues

##Transformacion de tipos de datos
varb = '5' + '4'
varb = int (varb)
print(varb+5)

## Tips
no se suman tipos de datos, se puede inprimir varias variables con comas " , " y no con " + "

#Estructuras de Control
## Condicionales

operador == da verdadero o falso porque lo compara
operador != desigualdad verifica si son diferentes

operadores logicos and, or y not


lower: minusculas
upper: mayusculas
count: contar
"""

edad = 19
if(edad > 18):
  print('Puede ser arrestado')
else:
    print('Es menor de edad')

vara = 5
varb = 2 + 8
print(varb + vara + 8)

varb = vara + 8
print(varb)

vara = 2
type(vara)

nombre = 'Luis'
nota = 20
print('el alumno {} es muy aplicado y tiene nota: '.format(nombre,nota))

varb = '5' + '4'
varb = int (varb)
print(varb+5)

print("Hello world")

numero=input('Ingrese el número: ')
if(int(numero) < 31):
  print('El número es menor de 31')
else:
  print('El número es correcto')

#El peso promedio de un adulto debe ser su estatura menos un metro
#, el rango aceptable es +-5kg, ejemplo si mido 1.60, mi peso promedio debe ser de 55kg a 65kg.
# Pídale al usuario que ingrese su estatura y verifique si está en el peso promedio.

estatura=int(input('Ingrese su estatura en metros: '))
estatura_en_centimetros=int(input('Ingrese su estatura en centimetros: '))

if(estatura_en_centimetros<50):
  print('Su peso es bajo')
else:
  print('Su peso es alto')

numero= int(input('Ingrese el número: '))
if(numero%2==0):
  print('El número es par')
else:
  print('El número es impar')

edad1=int(input('ingrese edad 1: '))
edad2=int(input('ingrese edad 2: '))
if(edad1> 18):
  print('La edad 1 es mayor de edad')
else:
  print('La edad 1 es menor de edad')
  if(edad2> 18):
    print('La edad 2 es mayor de edad')
  else:
    print('La edad 2 es menor de edad')

numero = 3
while(numero <= 100):
  numero = numero * 3
print(numero)

for i in range(2,23,3):
  print(i)

for i in range(99,-1,11):
  print(i)

nombre= "Hola"
print(nombre.swapcase())