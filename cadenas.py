import msvcrt
from os import replace

MSJ = "Presione una tecla para continuar..."

opt = 1

while opt == 1:
    cadena = ""
    letra = ""

    print("Ejercicios con STRING")
    sel = int(input("1. substring en string\n2. Repetición de una palabra en una cadena\n"
                    "3. Cuenta las palabras\n4. Reemplazar caracter\n5. Salir\n"))
    
    if sel == 1:
        cadena = input("Introduzca frase:\n")

        subcadena = input("Introduzca la palabra:\n")

        if cadena.isalpha() and subcadena.isalpha():
                if cadena.startswith(subcadena):
                    print("La frase ", cadena, " SI comienza con la palabra: ",subcadena)
                else:
                    print("La frase ", cadena, " NO comienza con la palabra: ", subcadena)
        else:
            print("No es una frase")
        

        print(MSJ)
        msvcrt.getch()
    
    if sel == 2:
        cadena = input("Ingrese la frase:\n")
        letra = input("Ingrese letra para contar: \n")

        if cadena.isalpha() and letra.isalpha():
            print("La letra: ", letra, " está en la frase: ", cadena, " ", cadena.count(letra), " veces")
        else:
            print("No es una frase")
            
        print(MSJ)
        msvcrt.getch()

    if sel == 3:
        cont = 0

        cadena = input("Ingrese la frase: \n")
        palabras = cadena.split()

        for i in palabras:
            if len(i) <= 2:
                cont += 1

        cantPalabras = len(palabras) - cont

        print("La frase: ", cadena, " tiene ", cantPalabras, " palabras")
        print(MSJ)
        msvcrt.getch()

    if sel == 4:
        cadena = input("Ingrese la frase: \n")
        char1 = input("Ingrese el caracter que quiere reemplazar: \n")
        char2 = input("Ingrese el remplazo del caracter anterior: \n")
        
        print("La nueva cadena es: ", cadena.replace(char1, char2))
        
        print(MSJ)
        msvcrt.getch()
    if sel == 5:
        opt += 1