"""
        Bienvenido al día 64 de #100díasdepython
                    El reto de hoy es:
    Utiliza regex para quitar los ceros innecesarios
        de las direcciones IP de la lista
    ["192.08.001.5", "10.120.023.001", "192.160.2.1" ]
    Imprime una lista con las IP validas
"""

import re

ip = ["192.08.001.5", "10.120.023.001", "192.160.2.1" ]
lista=[]

for c in ip:
    nueva = re.sub(r'\b0+(\d)', r'\1', c)
    lista.append(nueva)
print(lista)

    

    



