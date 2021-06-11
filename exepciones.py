
import msvcrt

MSJ = "Presione una tecla para continuar..."

opt = 1

class DivisionPorCero(Exception):
    """División por cero"""
    pass

while opt == 1:
    sel = int(input("1. División por cero\n2. Index fuera de la lista\n3. Llave no encontrada\n"
                    "4. Conversión de string a int\n5. Salir\n"))

    if sel == 1:
        try:
            result = 10 / 0
        except ZeroDivisionError:
            print(ZeroDivisionError)
            
        print(MSJ)
        msvcrt.getch()

    if sel == 2:
        try:
            lista = [1, 2, 3, 4, 5]
            print(lista[10])
        except IndexError:
            print(IndexError,"\nEl index seleccionado no existe en la lista...", lista)

        print(MSJ)
        msvcrt.getch()

    if sel == 3:
        try:
            colores = {'rojo':'red','verde':'green','negro':'black'}
            print(colores['blanco'])
        except KeyError:
            print(KeyError,"\nLa llave introducida no está en el diccionario...\n", colores)

        print(MSJ)
        msvcrt.getch()

    if sel == 4:
        try:
            print(5 + "20")
        except TypeError:
            print(TypeError,"\nUna cadena no puede ser operada con un número, antes debe ser\n"
                                "parseada al tipo de dato correspondiente...")

        print(MSJ)
        msvcrt.getch()

    if sel == 5:
        opt += 1
