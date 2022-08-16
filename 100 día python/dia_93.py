"""
        Bienvenido al día 93 de #'100díasdepython'
                    El reto de hoy es:
    Crea una fucion que use yield y genere los primeros 
    10 numeros de la serie  de Fibonacci
"""

def fibonacci(limite):
    ultimo, actual =0,1
    while limite > 0:
        yield actual
        ultimo, actual = actual, ultimo +actual
        limite -=1

serie = list(fibonacci(10))
print(serie)
        