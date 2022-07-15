"""
        Bienvenido al día 81 de #'100díasdepython'
                    El reto de hoy es:
        Utiliza datetime para agregarle a la fecha 
        actual 7 días mas, Imprime el resultado
    
"""

from datetime import datetime, timedelta

fecha = datetime.today()
fecha_futuro = fecha + timedelta(days=7)
print(fecha_futuro)