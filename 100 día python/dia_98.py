"""
        Bienvenido al día 98 de #'100díasdepython'
                    El reto de hoy es:
    Utiliza timeit para obtener el tiempo de ejecucion 
    de la siguiente funcion
    Imprime el resultado en una sola linea

"""

import timeit

def lazy():
    suma = 0
    for i in range(0, 50000000):
        suma += i

start = timeit.default_timer()
lazy()  
end = timeit.default_timer()
print(end - start)