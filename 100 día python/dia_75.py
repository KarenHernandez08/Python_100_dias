"""
        Bienvenido al día 75 de #'100díasdepython'
                    El reto de hoy es:
    Utiliza itertools para obtener el mensaje secreto en 
    la siguiente cadena 'P1y2t3h4o5n6!7'
    Imprime el resultado en una cadena 
  
"""

import itertools

cadena = 'P1y2t3h4o5n6!7'
selector = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
print("".join(itertools.compress(cadena, selector)))