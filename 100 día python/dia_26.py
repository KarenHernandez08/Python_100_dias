""" 
        Bienvenido al día 26 de #100díasdepython
                    El reto de hoy es:
    Utiliza la función copy() para crear una copia de la
    lista de compras utilizada en el reto anterior, compara
    sus ids en memoria e imprime el resultado
     
"""
compras=['leche', 'huevo', 'aceite', 'pan', 'tomate', 'manzana']

copia=compras.copy()

a=id(compras) == id(copia)
print(a)

