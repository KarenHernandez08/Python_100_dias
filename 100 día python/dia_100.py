"""
        Bienvenido al día 100 de #'100díasdepython'
                    El reto de hoy es:
    Utiliza try para capturar e imprimir la excepcion
    dentro  de la siguiente funcion y agrega un mensaje 
    final utilizando finally

"""

from typing import final


def dia100():
    try:
        mensaje ='Reto del día'
    except Exception as e:
        print ('Error: {}'.format(e))
    finally:
        print('Este es el ultimo reto')

dia100()