""" 
        Bienvenido al día 50 de #100díasdepython
                    El reto de hoy es:
    Genera 5 numeros enteros de forma aleatorio, 
    almacenalos en una lista, sumalos e imprime el resultado
     
"""

import random
lista=[random.randrange(1, 100) for i in range(5)]
suma=sum(lista)
print (suma) 