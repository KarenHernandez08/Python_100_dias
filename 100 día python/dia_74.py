"""
        Bienvenido al día 74 de #'100díasdepython'
                    El reto de hoy es:
        Utiliza itertools para obtener el producto 
        cartesiano de las siguientes listas
            [1, 3, 5] y [2, 4, 6]
        Imprime el resultado en una lista de tuplas
  
"""

import itertools

lista_a, lista_b = [1, 3, 5], [2, 4, 6]

producto = itertools.product(lista_a, lista_b)
resultado = list(producto)
print(resultado)