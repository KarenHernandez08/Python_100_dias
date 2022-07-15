"""
        Bienvenido al día 83 de #'100díasdepython'
                    El reto de hoy es:
    Utiliza datetime para convertir  la fecha  
    "jul 11 2022 1:30AM" al formato "2022-07-11 01:30:00"
    Imrpime el resultado
    
"""

from datetime import datetime

fecha = "Jul 11 2022 1:30AM"
resultado = datetime.strptime(fecha, "%b %d %Y %I:%M%p")
print(resultado)