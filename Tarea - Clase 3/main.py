from item2 import *
from item3 import *
import item4 as tienda
import item5
import item6
from item7 import *
import os

if __name__ == '__main__':
    
    print("----------------- ITEM 1 ------------")
    print("......")
    
    print("\n----------------- ITEM 2 ------------")
    print("Texto : ",texto)
    print("--->Split")
    print(texto_split())
    print("--->Join")
    print(texto_joined("_",texto))
    print("--->Count")
    resultado_count = texto_count(".")
    print(f"Existen {resultado_count} coincidencias")
    print("--->Find")
    resultado_find = texto_find("Lorem")
    print(f"La palabra buscada comienza en el indice {resultado_find}")
    print("--->UpperCase")
    print(texto_upperCase())
    print("--->LowerCase")
    print(texto_lower())

    print("\n----------------- ITEM 3 ------------")
    numero_multiplicar = 4
    print(f"El numero {numero_multiplicar} x 2 es = ",multi_2(numero_multiplicar))

    print("\n----------------- ITEM 4 ------------")
    catalogo = tienda.Catalogo()
    producto1 = tienda.Producto("Laptop", 800)
    producto2 = tienda.Producto("PC", 1500)
    catalogo.agregar_producto(producto1)
    catalogo.agregar_producto(producto2)
    catalogo.mostrar_productos()

    try:
        print("\n----------------- ITEM 5 ------------")
        item5.iniciar()
        n_numero = 5
        resultado = item5.suma_recursiva(n_numero)
        print(f"La suma recursiva de {n_numero} es : {resultado}")

        numerador = 10
        denominador = 2
        resultado2 = item5.dividir(numerador, denominador)
        print(f"El resultado de {numerador}/{denominador} es: {resultado2}")
        
    except Exception as e:
        print("\n Error: ", e)
        print("Ruta de trabajo: ", os.getcwd())
    finally:
        print("\nProceso terminado")

    print("\n----------------- ITEM 6 ------------")
    print(item6.nombreBase)

    print("\n----------------- ITEM 7 ------------")
    p1 = Producto("Producto1", "PERU-0001-2023")
    print(p1)
    print("País de origen: ",p1.identificar_pais())
    print("Número de lote: ",p1.identificar_lote())
    print("Año: ",p1.identificar_anio())
    