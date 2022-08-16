"""
        Bienvenido al día 95 de #'100díasdepython'
                    El reto de hoy es:
    Crea una funcion que use argumentos arbitrarios
    para recibir N-numeros y determine cual es el mayor y 
    el menor y los devuelva en un diccionario
"""

def mayor_menor(*numeros):
    mayor = max(numeros)
    menor = min(numeros)
    return {'mayor':mayor, 'menor':menor}

print(mayor_menor(1, 45, -3, -2, 9, 56))
