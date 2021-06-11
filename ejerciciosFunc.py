# Escriba una función que dado un número n calcule sus factores primos. 
#     La función debe retornar una lista con los números primos que descomponen el numero n. 
#     Ejemplo si n = 100, la descomposición en factores primos es [2,2,5,5]
#     (Numeros primos: 1 2 3 5 7 11 13 17 19 23...)

#     Instrucciones
#     Para solucionar este problema, el usuario debe crear una función llamada factores(n). 
#     Debe retornar una lista con los factores primos del numero dado. El número debe ser un 
#     numero natural mayor que 2. Por ejemplo, si n = 100, la operación de descomposición es: 
#     100/2 = 50 50/2 = 25 25/5 = 5 5/5 = 1 La lista que retorna la función factores(n) 
#     es [2,2,5,5] Por ejemplo, si el número es primo entonces la función factores(n) 
#     devuelve una lista con un solo elemento 11/11 = 1 La lista retorna [11]
# """

# """
#     Elabore un reloj analógico utilizando los metodos de las bibliotecas import
    
#     El sistema debe ir mostrando la hora segundo a segundo en el formato HH:MM:SS    
#     Ejemplo: 17:58:50
# """

import time
import os
from datetime import datetime

opt = 1

while opt == 1:
    now = datetime.now()

    print(now.day, "/", now.month, "/", now.year, "\n",
            f"\t{now.hour}:{now.minute}:{now.second}")

    print("\r"),
    time.sleep(1)

