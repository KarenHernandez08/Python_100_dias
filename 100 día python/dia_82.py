"""
        Bienvenido al día 82 de #'100díasdepython'
                    El reto de hoy es:
        Utiliza datetime para imprimir la fecha y hora 
        actual en el formato "10 July 2022, 12:12:12 AM"
        Imprime el resultado en una cadena
    
"""

from datetime import datetime

fecha = datetime.today()
formato = fecha.strftime("%d %B %Y, %I:%M:%S %p")
print (formato)