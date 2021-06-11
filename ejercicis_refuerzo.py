import msvcrt

MSJ = "Presione una tecla para continuar..."

opt = 1

while opt == 1:
    num = 0
    numList = []

    print("Ejercicios Refuerzo")
    sel = int(input("1. Multiplos de 6 entre 6 a 150\n2. Multiplos de n entre n y m * n\n3. Potencia de 2 entre 0 y 30"
                    "\n4. Sumatoria simple\n5. Factorial de un número positivo\n6. Salir\n"))

    if sel == 1:
        for i in range(6, 150 + 1):
            if i % 6 == 0:
                print(i)

        print(MSJ)
        msvcrt.getch()
    
    if sel == 2:
        num = input("Ingrese n y m separados por un espacio\nej: 6 7:\n")

        numList = num.split()

        for i in range(int(numList[0]), int(numList[1]) * int(numList[0]) + 1):
            if i % int(numList[0]) == 0:
                print(i)

        print(MSJ)
        msvcrt.getch()
    
    if sel == 3:
        num = int(input("Ingrese número para saber la potencia:\n"))

        for i in range(0, 20 + 1):
            print(num, "^",i," = ", num**i)
        
        print(MSJ)
        msvcrt.getch()
    
    if sel == 4:
        suma = 0

        num = input("Ingrese n y m separados por un espacio\nej: 6 7:\n")

        numList = num.split()

        if int(numList[0]) > int(numList[1]):
            print("n debe ser menor o igual que m")
        else:
            for i in range(int(numList[0]), int(numList[1]) + 1):
                suma += i
            print("Total de la sumatoria: ", suma)

        print(MSJ)
        msvcrt.getch()
    
    if sel == 5:
        fact = 1
        num = int(input("Ingrese número para saber el factorial:\n"))

        if num == 0:
            print("Factorial de ", num, " = 1")
        else:
            for i in range(1, num + 1):
                fact *= i
            print("Factorial de ", num, " es = {:,.0f}".format(fact))

        print(MSJ)
        msvcrt.getch()

    if sel == 6:
        opt += 1


