numeros= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
personas= [['Carlos', 20], ['Jose', 23], ['Maria', 15], ['Ana', 22]]

while True:
    print("Selecciona una opcion:")
    print("1. Dibujar un cuadrado en consola con *")
    print("2. Identificar si un número es múltiplo de 2")
    print("3. Imprimir solo los mayores de edad")
    print("4. Salir")
    opcion = int(input())
    if opcion == 1:
        size = int(input("Ingresa el tamaño del cuadrado: "))
        print("\n")
        for i in range(size):
            for j in range(size):
                print("*", end=" ")
            print()
    elif opcion == 2:
        print("Analizando la lista : ",numeros)
        for numero in numeros:
            if numero % 2 == 0:
                print("El numero ",numero, " es multiplo de 2")
    elif opcion == 3:
        print("Analizando la lista : ",personas)
        print("Mostrando personas mayores de edad :")
        for persona in personas:
            if persona[1] >= 18:
                print(persona[0]," tiene ",persona[1])
    elif opcion == 4:
        break
    else:
        print("Opcion invalida, selecciona una opcion valida.")

    print("\n")
    print("Fin del Progrrama")
    print("\n-----------------------------------------") 