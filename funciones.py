from math import sqrt, pi

import msvcrt

MSJ = "Presione una tecla para continuar..."

opt = 1

def RaizCuarta(num):
    if num < 0:
        print("No se admiten valores negativos")
    else:
        return print("Raíz cuarta de",num, " = " , sqrt(sqrt(num)))

def AreaCirculo(radio):
    return print("Área de un círculo con radio: ", radio, " es: ", round(pi * radio**2, 2))

def PrecVenta():
    infoProd = input("Ingrese el nombre y el costo del artículo separado por un espacio:\n")

    prodList = infoProd.split()

    nombre = prodList[0]
    costo = float(prodList[1])

    precioVenta = (costo * 1.2) + (costo * 0.15) + 2 * costo

    return print("Nombre: ", nombre, " Precio de venta: ", precioVenta)

while opt == 1:
    sel = int(input("1. Raíz cuarta\n2. Área de un círculo\n3. Precio de venta\n4. Salir\n"))

    if sel == 1:
        num = float(input("Ingrese número para saber la raíz cuarta\n"))
        RaizCuarta(num)
        print(MSJ)
        msvcrt.getch()

    if sel == 2:
        radio = float(input("Ingrese el valor del radio\n"))
        AreaCirculo(radio)
        print(MSJ)
        msvcrt.getch()

    if sel == 3:
        PrecVenta()
        print(MSJ)
        msvcrt.getch()

    if sel == 4:
        opt += 1
