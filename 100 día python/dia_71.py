"""
        Bienvenido al día 719 de #'100díasdepython'
                    El reto de hoy es:
    Utiliza itertools para generar una serie de sumas acumuladas 
    con los npumeros de la sigueinte lista [0, 1, 1, 2, 3, 5, 8]
    Imprime el resultado
"""
from itertools import *

lista =[0, 1, 1, 2, 3, 5, 8]
suma=list(accumulate(lista))
print(suma)