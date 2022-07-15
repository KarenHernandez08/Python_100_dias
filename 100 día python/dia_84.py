"""
        Bienvenido al día 84 de #'100díasdepython'
                    El reto de hoy es:
    Utiliza datetime para convertir la cadena 
    "12-07-2022" a timestamp, Imprime el resultado
    
"""

from datetime import datetime

cadena = "12-07-2022"
fecha =datetime.strptime(cadena, "%d-%m-%Y")
resultado = fecha.timestamp()
print(resultado)