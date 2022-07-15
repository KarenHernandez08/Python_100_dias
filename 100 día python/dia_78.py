"""
        Bienvenido al día 78 de #'100díasdepython'
                    El reto de hoy es:
  Utiliza itertools para unir las siguientes tuplas
    (78, 100) ("Dias", "Python") Obtiene el tipo de 
    cada dato e immprimelo en una lista
  
"""

import itertools

numeros = (78, 100)
cadenas = ("Dias", "Python")
lista = list(itertools.chain(numeros, cadenas))
resultado = [type(x) for x in lista]
print(resultado)