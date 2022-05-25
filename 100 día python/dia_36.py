""" 
        Bienvenido al día 36 de #100díasdepython
                    El reto de hoy es:
   Utiliza el diccionario del reto anterior para eliminar
   el primer elemento del diccionario, imprime la cantidad de elementos del
   diccionario 
     
"""


diccionario={
    "python": "Python es un lenguaje de programación de código abierto, interpretado y orientado a objetos",
    "Cadena":"Es una colección de uno o dos más caracteres bajo comillas simples o dobles",
    "Booleanos":  "Es un valor verdadero o falso: True or False",
    "Lista":"Es una colección ordenada que permite almacenar diferentes tipos de elementos de datos",
    "Diccionario":  "Es una colección desordenada de datos en un formato de par de valores clave"
    
}
diccionario.pop('python')
print(len(diccionario))
