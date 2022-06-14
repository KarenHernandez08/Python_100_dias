""" 
        Bienvenido al día 53 de #100díasdepython
                    El reto de hoy es:
    Crea una función que reciba una lista  de numeros
    y devuelva una lista de los numeros al cuadrrado
    Ejecuta la función para la lista [2,3,5,7,11]
    imprime el resultado
"""

lista=[2,3,5,7,11]

def cuadrado (lista):
    for i in range(0,len(lista)):
	    lista[i]=lista[i]*lista[i]
    return lista
    
print(cuadrado(lista))

