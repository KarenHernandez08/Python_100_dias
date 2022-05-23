""" 
        Bienvenido al día 33 de #100díasdepython
                    El reto de hoy es:
   Declara una cadena que sea un polindromo y verifica que lo sea
   sin usar funciones adicionales, imprime el resultado en una 
   sola línea
     
"""
x= "radar"
y= x[::-1]
polindromo= x == y
print(polindromo)
