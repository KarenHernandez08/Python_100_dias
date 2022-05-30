""" 
        Bienvenido al día 40 de #100díasdepython
                    El reto de hoy es:
    Utiliza el conjunto del reto anterior y elimina 
    el gato del conjunto, si es que existiera,imprime el resultado
     
"""

animales={'aguila', 'ballena', 'caracol', 'delfin', 'elefante'}
animales.discard('gato')

print(animales)