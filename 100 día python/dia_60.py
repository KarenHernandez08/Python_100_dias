"""
        Bienvenido al día 60 de #100díasdepython
                    El reto de hoy es:
    Utiliza una función lambda para capitalizar las 
            palabras de la siguiente lista
    ["llevo","sesenta", "dias", "programando", "wiii"]
            Imprime el resultado
"""


lista=["llevo","sesenta", "dias", "programando", "wiii"]

resultado = list(map(lambda c: c.capitalize(), lista))
print(resultado)