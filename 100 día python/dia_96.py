"""
        Bienvenido al día 96 de #'100díasdepython'
                    El reto de hoy es:
    Crea una funcion que use argumentos arbitrarios de 
    tipo keyword para recibir nombre, apellido y edad y 
    devuelva estos argumentos en un diccionario
"""

def persona(**atributos):
    resultado = dict()
    for key, value in atributos.items():
        resultado[key] = value
    return resultado

print(persona(nombre='karen', apellido='hernnadez', edad=23))