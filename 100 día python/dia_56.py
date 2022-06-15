""" 
        Bienvenido al día 56 de #100díasdepython
                    El reto de hoy es:
    Crea una función lambda para encontrar la raíz cuadrada
    de esta lista de numeros [49, 4, 36, 16, 25]
    Imprime el resultado en una lista nueva
"""

import math

mi_lista = [49, 4, 36, 16, 25]
lista_nueva = list(map(lambda x:  math.sqrt(x) , mi_lista))
print(lista_nueva)