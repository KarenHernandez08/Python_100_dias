""" 
        Bienvenido al día 55 de #100díasdepython
                    El reto de hoy es:
    Crea una función recursiva para hacer una cuenta regresiva a 0
    La funcion tiene como parametro de entrada un numero, ejecuta 
    la funcion para el numero 5, Imprime el valor de la cuenta en cada iteración
"""

numero=5
def cuenta_regresiva(numero):
    while 0 !=numero:
        print(numero)
        numero=numero-1
    return numero
    
cuenta_regresiva(numero)
    
  