""" 
        Bienvenido al día 57 de #100díasdepython
                    El reto de hoy es:
    Utiliza una función lambda para encontrar los 
    multiplos de 3 en la lista de numeros
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
    Imprime el resultado de una nueva lista
"""

lista=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nueva_lista=list(filter(lambda x:True if x % 3 == 0 else False, lista))
print(nueva_lista)