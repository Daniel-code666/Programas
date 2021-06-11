import msvcrt

opt = 1

MSJ = "Presione una tecla para continuar..."

while opt == 1:
    print("Ejercicios estructuras de repetición WHILE")
    sel = int(input("1. Fibonacci\n2. Suma números\n3. Monto de compras\n4. Salir\n"))

    if sel == 1:
        act, fibo = 1, 0

        num = int(input("Ingrese límite de la serie: \n"))

        i = 1

        # for i in range(0, num):
        #     act += fibo
        #     fibo = act - fibo
        #     print(fibo)

        while i <= num:
            act += fibo
            fibo = act - fibo
            print(fibo)
            i += 1

        print(MSJ)
        msvcrt.getch()

    if sel == 2:
        
        opt0, suma = 1, 0

        while opt0 == 1:
            numSum = float(input("Ingrese número: \n"))

            if numSum > 0:
                suma += numSum

            exit = int(input("¿seguir introduciendo números? SI=1/NO=0\n"))

            if exit == 0:
                opt0 += 1
                print("Suma: ", suma)

        print(MSJ)
        msvcrt.getch()

    if sel == 3:

        opt1, tot = 1, 0

        while opt1 == 1:
            compra = float(input("Introduzca el precio de cada artículo, si ingresa 0 el programa\n"
            "cortará el ingreso de datos\n"))
            
            while compra < 0:
                print("Escriba un valor válido...")
                compra = float(input("Introduzca el precio de cada artículo\n"))

            tot += compra

            if compra == 0:
                opt1 += 1
                print("Total", tot)
        
        print(MSJ)
        msvcrt.getch()

    if sel == 4:
        opt += 1

        print("Saliendo")
