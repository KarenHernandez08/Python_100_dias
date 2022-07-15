"""
        Bienvenido al día 73 de #'100díasdepython'
                    El reto de hoy es:
        Utiliza itertools para obtener todas las permutaciones
        posibles con las letras de la siguiente lidta 
                    ["r", "i", "o"]
        Imprime el resultado de una lista de tuplas
  
"""

import itertools

data = ["r", "i", "o"]
resultado = list(itertools.permutations(data))
print (resultado)