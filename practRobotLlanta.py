import random

rueda = random.randint(1,5)


if rueda < 3:
    print("Bombillo dañado")
    print("El robot está aprendiendo a desatornillar la llanta para quitarla")
    practicaRobot = random.randint(1,8)
    if practicaRobot > 4:
        print("El robot está aprendiendo ha identificar una llanta dañada")
        practicaRobot = random.randint(1,8)
        if practicaRobot > 5:
            print("El robot está reemplazando la nueva llanta")
            practicaRobot = random.randint(1,8)
            if practicaRobot > 6:
                print("El robot ha aprendido a cambiar la llanta")
            else:
                print("El robot no ha aprendido...")
        else:
            print("El robot no ha aprendido")
    else:
        print("El robot no ha aprendido")
else:
    print("La llanta no se ha dañado")
