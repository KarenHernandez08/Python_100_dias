"""
        Bienvenido al día 67 de #100díasdepython
                    El reto de hoy es:
    Utiliza regex para cambiar el formato de las fechas de YYYYMMDD a 
    YYYY-MM-DD de las fechas de la lista:
    ["20221205", "19930612", "20050126", "20211008"]
       Imprime una lista con las fechas 
"""


import re

fechas=["20221205", "19930612", "20050126", "20211008"]

formato=[re.sub(r'(\d{4})(\d{2})(\d{2})','\\1-\\2-\\3', fecha) for fecha in fechas]
print(formato)


