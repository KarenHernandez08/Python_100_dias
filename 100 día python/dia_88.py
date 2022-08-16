"""
        Bienvenido al día 88 de #'100díasdepython'
                    El reto de hoy es:
    Utiliza calendar para imprimir la cantidad de semanas
    en cada mes del año 2022
"""

from calendar import monthcalendar

semanas = [len(monthcalendar(2022, x))for x in range (1, 13)]
print(semanas)
