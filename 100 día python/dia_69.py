"""
        Bienvenido al día 69 de #'100díasdepython'
                    El reto de hoy es:
    Utiliza regex para extraer todas las 'a' seguidas de una o más 
    'b's de la siguiente cadena "abholaaaaabaaabbpythonistaaaaaabbbbb"
    imprime una lista con las subcadenas extraidas
"""

import re
cadena = "abholaaaaabaaabbpythonistaaaaaabbbbb"
patron =  'a+b'
buscar= re.findall(patron, cadena)
print(buscar)


