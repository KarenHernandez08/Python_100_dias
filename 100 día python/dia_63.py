"""
        Bienvenido al día 63 de #100díasdepython
                    El reto de hoy es:
    Utiliza regex para validar que las cadenas solo 
           contengan caracteres alfanumericos
    ["Python3.10", "python3", "ProgramandoAndo","jun2022",
       "#100diasdecodigo", "Felicidades!"]
       Imprime una lista con las cadenas validas
"""

import re
lista=["Python3.10",
       "python3",
       "ProgramandoAndo",
       "jun2022",
       "#100diasdecodigo",
       "Felicidades!"]
x="^[a-zA-z0-9_]+$"

alfanumericos=[c for c in lista if re.search(x,c)]
print(alfanumericos)