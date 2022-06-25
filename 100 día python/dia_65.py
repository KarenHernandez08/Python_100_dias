"""
        Bienvenido al día 65 de #100díasdepython
                    El reto de hoy es:
    Utiliza regex para quitar los prefijos telefonicos 
    de los telefonos de la siguiente lista
   ["+54 11 1234 5678", "+591 68754321", "+56 9 8765 4321"]
   Imprime una lista con los telefonos sin prefijos telefonicos
""" 

import re
telefonos=["+54 11 1234 5678", "+591 68754321", "+56 9 8765 4321"]
prefijos=[re.sub("\+[0-9]* ", "", tel)for tel in telefonos]
print(prefijos)
