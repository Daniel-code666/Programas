from math import pow, pi

dividendo, varianza, sumNum = 0, 0, 0

opt = 1

while opt == 1:
    print("Ejercicios varios\n¿Qué desea hacer? Seleccione ingresando un número")
    
    sel = int(input("1. Varianza\n2. Promedio\n3. Área círculo\n 4. Cálculo de IVA\n5. Salir"))

    if sel == 1:
        num = input("Ingrese los números separados por un espacio\nej: 1 2 3 4\n")

        numList = num.split()

        for i in range(0, len(numList)):
            sumNum += int(numList[i])

        prom = sumNum / len(numList)

        for i in range(0, len(numList)):
            dividendo += pow((int(numList[i]) - prom), 2)

        dividendo /= len(numList)

        print(dividendo)

    if sel == 2:
        sumNum = 0

        num = input("Ingrese los números separados por un espacio\nej: 1 2 3 4\n")

        numList = num.split()

        for i in range(0, len(numList)):
            sumNum += int(numList[i])

        prom = sumNum / len(numList)

        print("Media: ", prom)

    if sel == 3:
        radio = int(input("Ingrese el valor del radio: "))

        area = pi * radio * radio

        print("Área del círculo: ", "{0:.2f}".format(area))

