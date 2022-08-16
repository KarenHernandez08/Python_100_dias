"""
        Bienvenido al día 86 de #'100díasdepython'
                    El reto de hoy es:
    Utiliza datetime para calcular ;a cantidad de segundo que han 
    pasado desde el inicio del reto considerando solo la fecha 20/04/2022
    Imprime el resultado
"""
from datetime import datetime

inicio = datetime.strptime('20/04/2022', '%d/%m/%Y')
dia86 = datetime.strptime('14/07/2022', '%d/%m/%Y') 
segundos = (dia86 - inicio).total_seconds()
print(segundos)