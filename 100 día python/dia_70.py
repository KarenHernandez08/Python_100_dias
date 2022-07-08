"""
        Bienvenido al día 70 de #'100díasdepython'
                    El reto de hoy es:
    Utiliza regex para extraer todas las palabras que contengan al menos 
    una 'a' en la siguiente cadena, "Llevas programando 70 dias seguidos"
"""


import re

cadena = "Llevas programando 70 dias seguidos"
patron = r'\w*a.\w*'


palabras = re.findall( patron, cadena)
print(palabras)

