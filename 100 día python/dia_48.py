
""" 
        Bienvenido al día 48 de #100díasdepython
                    El reto de hoy es:
    Con un rango de 5 numeros crea una lista que refleje
    con valores booleanos cuales son los pares e imprime
    el resultado
"""
numeros=list(range(1,6))

for i in numeros:
    if (i%2)==0:
        print(True)
        i=False 
    else:
        print(False)
        
        
      
        
  