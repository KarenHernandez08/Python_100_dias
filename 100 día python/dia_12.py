""" 
        Bienvenido al día 12 de #100díasdepython
                El reto de hoy es:
    Intercambia los valores de dos variables e imprime su ubicacion en memoria
                            utilizando la funcion id()

"""

a=5
b=7

b,a=a,b

print(id(a), id(b))
