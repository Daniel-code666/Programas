from random import randint
import msvcrt
from cmath import sqrt

MSJ = "Presione una tecla para continuar..."

opt = 1

def diasAnio(year):
    bisiesto = False
    
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        bisiesto = True
    else:
        bisiesto = False   

    return bisiesto

def funcTriPerf():
    
    puntos = []

    lim = input("Ingrese z1 y z2: \n")
    
    limList = lim.split()

    while limList[1] < limList[0]:
        lim = input("El valor de z2 debe ser mayor que z1: \n")
        limList = lim.split()

    a, b, c = randint(1, 10), randint(1, 10), randint(1, 10)
    
    z1, z2 = round(float(limList[0])), round(float(limList[1]))
    
    for i in range(z1, z2 + 1):
        x = a*i**2 + b*i + c
        puntos.append(x)

    return print(puntos, max(puntos), min(puntos))

while opt == 1:
    
    try:
        sel = int(input("1. Cuadrática\n2. Días del año\n3. Salir\n"))
        
        if sel == 1:
            funcTriPerf()

            print(MSJ)
            msvcrt.getch()    
        
        if sel == 2:
            year = int(input("Ingrese año:\n"))

            if diasAnio(year):
                print("El año:", year, " es bisiesto y tiene 366 días")
            else:
                print("El año:", year, " no es bisiesto y tiene 365 días")

            print(MSJ)
            msvcrt.getch()

        if sel == 3:
            opt += 1

    except ValueError:
        print(ValueError, "Ingrese una opción en forma de número entero")