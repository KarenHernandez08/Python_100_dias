""" 
        Bienvenido al día 54 de #100díasdepython
                    El reto de hoy es:
    Crea una función que reciba una lista de cadenas y 
    devuelva un diccionario con la cantidad de vocales de cada cadena
    ejemplo de entrada: ['Python', 'es', 'cool']
    ejemplo de salida:{'python': 1, 'es': 1, 'cool': 2}
    
    imprime el resultado
"""

lista=['Python', 'es', 'cool']

def contar_vocales(lista):
    diccionario={}
    cadena=[x.lower()for x in lista]
    for lista in cadena:
        contador=0
        for vocal in 'aeiou':
            contador+=lista.count(vocal)
            diccionario[lista]=contador
    return diccionario

print(contar_vocales(lista))