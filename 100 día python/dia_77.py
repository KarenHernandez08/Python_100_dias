"""
        Bienvenido al día 77 de #'100díasdepython'
                    El reto de hoy es:
    Utiliza el itertools para obtener los multiplos 
    de 5 de la siguiente lista:
                [1, 5, 10, 23, 3, 555, 11, 10]
            Imprime el resuitado en una lista
  
"""

import itertools

lista = [1, 5, 10, 23, 3, 555, 11, 10]
predicado = lambda x: x % 5 !=0
multiplos = list(itertools.filterfalse(predicado, lista))
print(multiplos)