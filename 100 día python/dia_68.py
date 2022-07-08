"""
        Bienvenido al día 68 de #100díasdepython
                    El reto de hoy es:
    Utiliza regex para cambiar el formato de las fechas de 
    YYYY-MM-DD a DDMMYYYY de la siguiente lista
    ['2022-12-05', '1993-06-12', '2005-01-26', '2021-10-08']
    Imprime una lista con las fechas con el nuevo formato
"""
import re
lista= ['2022-12-05', '1993-06-12', '2005-01-26', '2021-10-08']
fechas= [re.sub(r'(\d{4})-(\d{2})-(\d{2})','\\3\\2\\1', fecha) for fecha in lista]

print(fechas)

