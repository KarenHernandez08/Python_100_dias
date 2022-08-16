"""
        Bienvenido al día 92 de #'100díasdepython'
                    El reto de hoy es:
    Crea una funcion que use yield y genere la siguiente serie
    [1, 2, 3, 1, 2, 3, 2, 1]
"""  

from re import I


def sube_baja(limite):
    i = j = 1
    k = 3
    while limite > 0:
        yield i 
        i = i + j
        j = -1 if i >= k else 1 if i <= 1 else j
        limite -= 1
        
lista = list(sube_baja(9))
print(lista)