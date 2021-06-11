import msvcrt

MSJ = "Presione una tecla para continuar..."

opt = 1

def dicInputVal():
    num = int(input("Ingrese número: \n"))
    dic = {}
    for i in range(1, num + 1):
        dic[i] = i**2
        
    return dic

def dicCaracter():
    cadena = input("Ingrese cadena de texto:\n")
    dicChar = {}
    for i in cadena:
        if not i in dicChar:
            dicChar[i] = cadena.count(i)
        
    return dicChar

def precFrutas():
    frutas = {"Manzana": 500, "Pera": 700, "Melón": 950}

    infoFruta = input("Ingrese el nombre de la fruta y la cantidad  vendida\n")

    info = infoFruta.split()

    if info[0] in frutas:
        return print("El precio final de la fruta es: ",float(frutas[info[0]]) * float(info[1]))
    else:
        return print("El dato ingresado no está en el diccionario")

while opt == 1:
    sel = int(input("1. Diccionario valor ingresado\n2. Diccionario con caracteres\n3. Diccionario precios de frutas"
                    "\n4. Salir\n"))

    if sel == 1:
        print(dicInputVal())

        print(MSJ)
        msvcrt.getch()

    if sel == 2:
        print(dicCaracter())
        
        print(MSJ)
        msvcrt.getch()

    if sel == 3:
        precFrutas()
        
        print(MSJ)
        msvcrt.getch()

    if sel == 4:
        opt += 1