"""
        Bienvenido al día 62 de #100díasdepython
                    El reto de hoy es:
    Utiliza regex para validar que la lista de emails
    ['pythonlapaz@gmail.com', 'dias.com', 'comidita@.com', 
    'programando@outlook.com']
    Imprime una lista con emails validos
"""

import re

correos=['pythonlapaz@gmail.com', 'dias.com', 'comidita@.com', 'programando@outlook.com']
regex = r'\b@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
correos_validos=[c for c in correos if re.search (regex,c)]
print(correos_validos)