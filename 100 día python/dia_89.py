"""
        Bienvenido al día 89 de #'100díasdepython'
                    El reto de hoy es:
    Utiliza calendar para obtener los días ;unes
    del mes de julio del año 2022
"""
from calendar import monthcalendar

lunes =[s[0]for s in monthcalendar(2022, 7) if s[0] !=0]
print(lunes)