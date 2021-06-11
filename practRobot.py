import random

bombillo = random.randint(1,5)

if bombillo < 3:
    print("Bombillo dañado")
    print("El robot está aprendiendo a girar el bombillo para quitarlo")
    practicaRobot = random.randint(1,5)
    if practicaRobot >= 2:
        print("El robot está aprendiendo ha identificar un bombillo dañado a uno que no")
        practicaRobot = random.randint(1,5)
        if practicaRobot >= 3:
            print("El robot está reemplazando el nuevo bombillo")
            practicaRobot = random.randint(1,5)
            if practicaRobot >= 4:
                print("El robot ha aprendido a cambiar un bombillo. \nBombillo cambiado")
            else:
                print("El robot no ha aprendido...")
        else:
            print("El robot no ha aprendido")
    else:
        print("El robot no ha aprendido")
else:
    print("El bombillo no se ha dañado")

