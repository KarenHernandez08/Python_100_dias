"""
        Bienvenido al día 97 de #'100díasdepython'
                    El reto de hoy es:
    Crea una funcion que use argumentos arbitrarios
    de tipo keyword para recibir los 3 lados de un
    triangulo y calcule su perimetro

"""

def perimetro(**atributos):
    a = atributos['a']
    b = atributos['b']
    c = atributos['c']
    return float(a+b+c)

print(perimetro(a=3, b=4, c=4))