""" 
        Bienvenido al día 51 de #100díasdepython
                    El reto de hoy es:
    Crea una función que calcule el volumen de un cilindro
    los parametros de entrada son diametro y altura, el valor de
    salida es el volumen del cilindro
    Ejecuta la función para el caso base=5, altura=7
    imprime el resultado
"""

from math import pi

def volumen(diametro=5, altura=7):
    radio=diametro/2
    v= pi* radio**2 *altura
    return v

print(volumen())