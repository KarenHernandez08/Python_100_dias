"""
        Bienvenido al día 86 de #'100díasdepython'
                    El reto de hoy es:
    Utiliza datetime para imprimir la fecha y hora en formato de 12 horas
"""

from datetime import datetime

fecha = datetime.today()
formato = fecha.strftime('%Y/%m/%d  %I:%M %p')
print(formato)