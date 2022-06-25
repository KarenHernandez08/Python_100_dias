""" 
        Bienvenido al día 59 de #100díasdepython
                    El reto de hoy es:
    Utiliza una función lambda para ordenar de forma ascendente
    la siguiente lista de tuplas comando el valor numerico como 
    referencia ("Quimica",88),("Fisica",90),("Lenguaje",97)
    imprime el resultado
"""


mi_lista = [("Quimica",88),("Fisica",90),("Lenguaje",97)]
mi_lista.sort(key=lambda x: x[1])
print(mi_lista)