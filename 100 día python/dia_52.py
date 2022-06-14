""" 
        Bienvenido al día 52 de #100díasdepython
                    El reto de hoy es:
    Crea una función que convierta un numero entero en binario 
    sin usar la funcion bin()
    El parametro de entrada es un numero entero
    El valor de salida es una cadena del valor del numero en binario
    
    Ejecuta la función para el numero 52, imprime el resultado
"""
def convertir(numero):
    binario = 0
    i = 1
    while numero != 0:
        binario = binario + numero % 2 * i
        numero //= 2
        i*= 10
        
    return binario


print(convertir(52))