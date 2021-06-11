# Necesitamos crear un programa que dado un numero aleatorio me permita X cantidad de intentos para adivinarlo y 
# en cada intento me vaya indicando si mi numero estimado es muy alto o muy bajo y en caso de no adivinar el 
# numero me indique que no pude adivinar dicho numero

import random

numMag, cont, num = random.randint(1,20), 0, 0

print("Adivine el número \n Tiene 8 intentos")

while num != numMag:
    num = int(input("Ingrese número: "))
    
    cont += 1

    if num > numMag:
        print("Muy alto. Lleva: ", cont, " intentos")
    elif num < numMag:
        print("Muy bajo. Lleva: ", cont, " intentos")
    else:
        print("Correcto, ha adivinado el número en: ", cont, " intentos")

    if cont >= 8:
        print("Ha excedido el número de intentos \n número a adivinar: ", numMag)
        break;

