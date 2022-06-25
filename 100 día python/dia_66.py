"""
        Bienvenido al día 66 de #100díasdepython
                    El reto de hoy es:
    Utiliza regex para eliminar los caracteres que 
    no sean alfanumericos en las cadenas de la siguiente lista
    ["Python3.10", "python3", "ProgramandoAndo","jun2022",
       "#100diasdecodigo", "Felicidades!"]
       Imprime una lista con las cadenas validas
"""

import re
lista=["Python3.18",
       "Python3",
       "ProgramandoAndo",
       "jun2022",
       "#100diasdecodigo",
       "Felicidades!"]

alfanumericos= [re.sub(r'[\W_]+', '', c)for c in lista]

print(alfanumericos)

