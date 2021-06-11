import msvcrt

from cmath import sqrt

MSJ = "Presione una tecla para continuar..."

opt = 1

def factorial(num):
    if num == 1 or num == 0:
        num = 1
        return num
    else:
        return num * factorial(num - 1)

def combinacion():
    
    valores = input("Ingrese n y m:\n")

    listaNM = valores.split()

    n = factorial(float(listaNM[0]))
    m = factorial(float(listaNM[1]))
    n_m = factorial(float(listaNM[0]) - float(listaNM[1]))

    return print(n / (n_m * m)) 

def sumatoria():
    suma = 0

    num = input("Ingrese n y m separados por un espacio\nej: 6 7:\n")

    numList = num.split()

    if int(numList[0]) > int(numList[1]):
        return print("n debe ser menor o igual que m")
    else:
        for i in range(int(numList[0]), int(numList[1]) + 1):
            suma += i
        return print("Total de la sumatoria: ", suma)

def funcCuadratica():
    puntos = []

    lim = input("Introduzca los valores de a, b, c, los límites z1 y z2: \n")

    limList = lim.split()

    a, b, c = float(limList[0]), float(limList[1]), float(limList[2])
    z1, z2 = int(limList[3]), int(limList[4])
    
    for i in range(z1, z2):
        x1 = (-b / 2 * a) + (sqrt(b**2 - 4 * a * c) / 2 * a) 
        x2 = (-b /  2 * a) - (sqrt(b**2 - 4 * a * c) / 2 * a)
        puntos.append(x1)
        puntos.append(x2)
    
    return puntos

def diasAnio(year):
    bisiesto = False
    
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        bisiesto = True
    else:
        bisiesto = False   

    return bisiesto

def esPrimo(num):
    if num % 2 ==0:
        return False
    else:
        return True

def primos(num):
    primosList = []
    for i in range(0, num + 1):
        if i % 2 != 0:
            primosList.append(i)

    return print(primosList)

def cuota():
    valores = input("Ingrese los valores de euros(h), años(n) e interés(i)\n")
    valList = valores.split()

    r = (float(valList[2]) / 100) / (100 * 12)

    m = float(valList[0]) * r / (1 - (1 + r)**(-12 * int(valList[1])))

    valList.append(m)
    
    return valList

while opt == 1:
    sel = int(input("1. Combinación\n2. Sumatoria\n3. Función cuadrática\n4. Número de días según su año"
                    "\n5. Número primo\n6. Cálculo de cuota\n7. Salir\n"))

    if sel == 1:
        combinacion()

        print(MSJ)
        msvcrt.getch()
    
    if sel == 2:
        sumatoria()

        print(MSJ)
        msvcrt.getch()

    if sel == 3:
        funcCuadratica()

        print(MSJ)
        msvcrt.getch()

    if sel == 4:
        year = int(input("Ingrese año:\n"))

        if diasAnio(year):
            print("El año:", year, " es bisiesto y tiene 366 días")
        else:
            print("El año:", year, " no es bisiesto y tiene 365 días")

        print(MSJ)
        msvcrt.getch()

    if sel == 5:
        num = int(input("Ingrese número:\n"))
        
        if esPrimo(num):
            print("Es primo")
            primos(num)
        else:
            print("No es primo")
        
        print(MSJ)
        msvcrt.getch()

    if sel == 6:
        cuotaInfo = cuota()
        print("La cantidad a pagar de:", cuotaInfo[0], " euros al mes para amortizar una hipoteca\n"
                " de ", round(cuotaInfo[3], 2), " en ", cuotaInfo[1], " años a un interés del:", 
                float(cuotaInfo[2]) * 10, "'%' anual")

        print(MSJ)
        msvcrt.getch()

    if sel == 7:
        opt += 1

