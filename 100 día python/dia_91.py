"""
        Bienvenido al día 91 de #'100díasdepython'
                    El reto de hoy es:
    Crea una función que devuelva los cuadrados de los
    primeros 10 numeros enteros iniciando en 1 utilizando
    yields
    
"""

from re import I


def cuadrados (limite):
    i = 1
    while i <= limite:
        yield i * i  
        i += 1
        
lista = list(cuadrados(10))
print(lista)