"""
        Bienvenido al día 61 de #100díasdepython
                    El reto de hoy es:
    Utiliza regex ára validar que las cadenas de la 
            lista sean totalmente numericas 
    ["20200806", "jun122022", "202204DD", "20221208", "22mar2022"]
    Imprime una lista con las cadenas númericas
"""
import re

lista=["20200806", "jun122022", "202204DD", "20221208", "22mar2022"]

x= '[\d]{8}'

numericos=[c for c in lista if re.search (x,c)]
print(numericos)

