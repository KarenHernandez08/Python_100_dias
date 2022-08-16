"""
        Bienvenido al día 94 de #'100díasdepython'
                    El reto de hoy es:
    Crea una funcion que use argumentos arbitrarios
    para recibir N-cadenas de nombres y devuelva una lista de 
    N-saludos
"""
def saludos(*nombres):
    resultado = ['Hola ' + n for n in nombres]
    return resultado

lista = saludos('Karen', 'Jocelyn', 'Roberto')
print(lista)