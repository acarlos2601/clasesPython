def iniciar():
        print("Iniciando Libreria")
def suma_recursiva(n):
    if n == 0:
        return 0
    else:
        return n + suma_recursiva(n-1)

def dividir(a, b):
    return a / b