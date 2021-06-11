from math import pow, pi
import msvcrt

MSJ = "Presione una tecla para continuar..."

opt = 1

while opt == 1:
    print("Ejercicios varios\n¿Qué desea hacer? Seleccione ingresando un número")
    
    sel = int(input("1. Varianza\n2. Promedio\n3. Área círculo\n4. Cálculo de IVA\n5. Cambiar pesos a dolares\n"
                    "6. Valor absoluto\n7. Masa\n8. Pulsos\n9.Incremento de salario\n10. Presupuestos"
                    "\n11. Salario + hrs extras\n12. Descuento\n13. Descuento computadoras\n14. Salir\n"))

    if sel == 1:
        #ejemplo:  2 3 6 8 11
        #varianza = 10.8

        dividendo, varianza, sumNum = 0, 0, 0

        num = input("Ingrese los números separados por un espacio\nej: 1 2 3 4\n")

        numList = num.split()

        for i in range(0, len(numList)):
            sumNum += float(numList[i])

        prom = sumNum / len(numList)

        for i in range(0, len(numList)):
            dividendo += pow((float(numList[i]) - prom), 2)

        dividendo /= len(numList)

        numList.append(dividendo)

        print(numList[-1])

        print(MSJ)
        msvcrt.getch()

    if sel == 2:
        sumNum = 0

        num = input("Ingrese los números separados por un espacio\nej: 1 2 3 4\n")

        numList = num.split()

        for i in range(0, len(numList)):
            sumNum += int(numList[i])

        prom = sumNum / len(numList)

        print("Media: ", prom)

        print(MSJ)
        msvcrt.getch()

    if sel == 3:
        radio = int(input("Ingrese el valor del radio: "))

        area = pi * radio * radio

        print("Área del círculo: ", "{0:.2f}".format(area))
        
        print(MSJ)
        msvcrt.getch()

    if sel == 4:
        costoProd = int(input("Ingrese el precio del producto: "))
        costoProd *= 0.16
        print("Costo de producto con IVA del 16%: ", costoProd)

        print(MSJ)
        msvcrt.getch()

    if sel == 5:
        
        pesos = float(input("Ingrese cantidad en pesos: "))

        while pesos < 0:
            print("Introduzca una cantidad válida")
            pesos = float(input("Ingrese cantidad en pesos: "))

        dolares = abs(pesos) / 3735.50

        print("Pesos: ", pesos, " a dolares: ", round(dolares, 3))
        print(MSJ)
        msvcrt.getch()

    if sel == 6:
        num = float(input("Ingrese número para conocer su valor absoluto: "))
        print("Valor absoluto: ", abs(num))
        print(MSJ)
        msvcrt.getch()

    if sel == 7:
        valores = input("Ingrese los valores en el siguiente orden: Presión, volumen y temperatura"
                        "\nEjemplo: 2 0 6:\n")
        valList = valores.split()

        masa = (float(valList[0]) * float(valList[1])) / (0.37 * (float(valList[2]) + 460))

        print("Valor de la masa: ", round(masa, 4))
        print(MSJ)
        msvcrt.getch()

    if sel == 8:
        edad = int(input("Ingrese la edad: "))

        numPulsos = (220 - edad) / 10

        print("Número de pulsaciones por cada 10 seg de ejercicio: ", numPulsos)
        print(MSJ)
        msvcrt.getch()

    if sel == 9:
        salario = float(input("Ingrese salario: "))
        
        print("Salario actual: ", salario, "\nNuevo salario: ", salario * 0.33)
        print(MSJ)
        msvcrt.getch()

    if sel == 10:
        presupuesto = float(input("Ingrese cantidad del presupuesto: "))

        while presupuesto < 0:
            print("Ingrese una cantidad válida...")
            presupuesto = float(input("Ingrese cantidad del presupuesto: "))
        
        print("Presupuesto para Ginecología: ", presupuesto * 0.40,
                "\nPresupuesto para Traumatología: ", presupuesto * 0.30,
                "\nPresupuesto para Pediatría: ", presupuesto * 0.30)

        print(MSJ)
        msvcrt.getch()

    if sel == 11:
        infoSal = input("Ingrese los valores del valor por hora y las horas trabajadas separados por espacios\n"
                        "ejemplo:5600 23\n")
        
        listaSalario = infoSal.split()

        precHora, hrsTrab = float(listaSalario[0]), float(listaSalario[1])

        if hrsTrab > 40:
            hrsExtra = hrsTrab - 40
            
            if hrsExtra < 8:
                totExtra = precHora * hrsExtra * 2
            else:
                totDoble = 8 * precHora * 2
                totTriple = (hrsExtra - 8) * precHora * 3
                totExtra = totDoble + totTriple

            pagoTot = 40 * precHora + totExtra
        else:
            pagoTot = precHora * hrsTrab

        print("El salario es: ", pagoTot)
        print(MSJ)
        msvcrt.getch()

    if sel == 12:
        elemnt = input("Ingrese el precio del artículo y el color de la etiqueta\n")

        elemntList = elemnt.split()

        precio, etiqueta = elemntList[0], elemntList[1]
        
        if etiqueta == "blanco":
            print("El precio es: ", precio)

        if etiqueta == "verde":
            print("El precio tiene un 10% de descuento: ", float(precio) - float(precio) * 0.10)

        if etiqueta == "amarilla":
            print("El precio tiene un 25% de descuento: ", float(precio) - float(precio) * 0.25)

        if etiqueta == "azul":
            print("El precio tiene un 50% de descuento: ", float(precio) - float(precio) * 0.50)

        if etiqueta == "roja":
            print("El artículo es gratis...")

        print(MSJ)
        msvcrt.getch()

    if sel == 13:
        
        precCompu = 3500000.4251

        cantCompu = int(input("Ingrese cantidad de computadoras compradas: "))

        if cantCompu >= 1 and cantCompu < 5:
            precCompu *= cantCompu
            totPrec = precCompu - precCompu * 0.10
        
        if cantCompu >= 5 or cantCompu < 10:
            precCompu *= cantCompu
            totPrec = precCompu - precCompu * 0.20

        if cantCompu >= 10:
            precCompu *= cantCompu
            totPrec = precCompu - precCompu * 0.40

        print("Precio total: ", "${:,.2f}".format(totPrec))
        print(MSJ)
        msvcrt.getch()
        
    if sel == 14:
        print("Saliendo...")
        opt += 1
    
    if sel > 14 or sel < 0:
        print("Opción ingresada no válida")
        print(MSJ)
        msvcrt.getch()
