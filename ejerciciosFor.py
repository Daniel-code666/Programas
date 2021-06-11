import msvcrt

MSJ = "Presione una tecla para continuar..."

opt = 1

while opt == 1:
    print("Ejercicios FOR")

    sel = int(input("¿Qué desea hacer?\n1. Suma negativos, promedio positivos\n2. Leap year\n3. Salir\n"))

    if sel == 1:
        sumNeg, sumPos, cont = 0, 0, 0

        for i in range(1, 7):
            print("Ingrese número en la posición ", i,":")
            num = float(input())

            if num < 0:
                sumNeg += num
            else:
                cont += 1
                sumPos += num

        if cont > 0:
            promPos = sumPos / cont
        else:
            promPos = 0

        print("Suma de número negativos:", sumNeg, "\nPromedio de números positivos: ", promPos)

        print(MSJ)
        msvcrt.getch()

    if sel == 2:

        year = input("Introduzca dos años separados por un espacio\nEj: 1987 2019\n")
        yearList = year.split()
        
        for i in range(int(yearList[0]), int(yearList[1]) + 1):
            if i % 4 == 0:
                if i % 100 == 0:
                    if i % 400 == 0:
                        if i % 10 == 0:
                            print(i)
                else:
                    if i % 10 == 0:
                            print(i)

        print(MSJ)
        msvcrt.getch()

    if sel == 3:
        opt += 1