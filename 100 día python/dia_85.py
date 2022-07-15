"""
        Bienvenido al día 85 de #'100díasdepython'
                    El reto de hoy es:
    Utiliza datetime para imprimir la fecha y hora actual
    en UTC
        
"""

from datetime import datetime, timezone

utc = datetime.now (timezone.utc)
print(utc)
