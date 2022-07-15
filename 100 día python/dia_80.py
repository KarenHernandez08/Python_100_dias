"""
        Bienvenido al día 80 de #'100díasdepython'
                    El reto de hoy es:
    Utiliza itertools para repetir el numero 80 5 veces
    en una lista, Imprime el resultado en una lista
  
"""

import itertools

lista = list(itertools.repeat(80, 5))
print(lista)