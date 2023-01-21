print("EJERCICIO 1")
print("------------------------------------------------------------")

nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
hobbie = input("Ingresa tus Hobbies: ")

print("_____")
print("Los datos que ingresaste son:")
print("Nombre:", nombre)
print("Edad:", edad)
print("Hobbie:", hobbie)



print("\n")
print("EJERCICIO 2")
print("------------------------------------------------------------")

import math

print("Programa para calcular areas")
radio = float(input("Ingresa el radio: "))

area_circulo = math.pi * radio ** 2

base = 2 * radio
altura = radio
area_triangulo = (base * altura) / 2

lado = 2 * radio
area_cuadrado = lado ** 2

print("_____")
print("Area del circulo:", area_circulo)
print("Area del triangulo:", area_triangulo)
print("Area del cuadrado:", area_cuadrado)



print("\n")
print("EJERCICIO 3")
print("------------------------------------------------------------")

valor1 = float(input("Ingresa el valor 1: "))
valor2 = float(input("Ingresa el valor 2: "))
valor3 = float(input("Ingresa el valor 3: "))

suma = valor1 + valor2 + valor3
resta = valor1 - valor2 - valor3
multiplicacion = valor1 * valor2 * valor3
division = valor1 / valor2 / valor3
division_entera = valor1 // valor2 // valor3

print("_____")
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicacion:", multiplicacion)
print("Division:", division)
print("Division Entera:", division_entera)



print("\n")
print("EJERCICIO 4")
print("------------------------------------------------------------")

valor = input("Ingresa un valor: ")

print("_____")
if valor.isalpha():
    print(type(valor))

elif valor.isnumeric():
    print(type(1))
else:
    print(type(valor))


print("\n")
print("EJERCICIO 5")
print("------------------------------------------------------------")

import sys

ubicacion = sys.argv[0]

print("La ubicación de la carpeta es: ", ubicacion)


print("\n")
print("EJERCICIO 6")
print("------------------------------------------------------------")

valor = int(input("Ingresa el numero: "))

suma = 0

for i in range(1, valor + 1):
    suma += i

print("_____")
print("La suma de los numeros hasta", valor, "es:", suma)


print("\n")
print("EJERCICIO 7")
print("------------------------------------------------------------")

numero1 = int(input("Ingresa el primer numero: "))
numero2 = int(input("Ingresa el segundo numero: "))

print("_____")
if numero1 == numero2:
    print("Los dos numeros son iguales.")
elif numero1 != numero2:
    print("Los dos numeros son diferentes.")
    if numero1 > numero2:
        print("El primer numero es mayor que el segundo.")
    elif numero2 >= numero1:
        print("El segundo numero es mayor o igual que el primero.")


print("\n")
print("EJERCICIO 8")
print("------------------------------------------------------------")

contraseña = "contraseña"

contraseña_ingresada = input("Ingresa la contraseña: ")

contraseña = contraseña.lower()
contraseña_ingresada = contraseña_ingresada.lower()

print("_____")
if contraseña_ingresada == contraseña:
    print("La contraseña es correcta.")
else:
    print("La contraseña es incorrecta.")


