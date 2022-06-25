""" 
        Bienvenido al día 58 de #100díasdepython
                    El reto de hoy es:
    Utiliza una función lambda para sumar la lista a con la lista b, 
    imprime el resultado en una nueva lista
"""

lista_a=[2,4,5]
lista_b=[6,7,1]
suma = list(map(lambda x, y : x + y, lista_a, lista_b))
print(suma)


