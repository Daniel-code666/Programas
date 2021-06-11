from math import fabs, sqrt
from random import randint

import msvcrt

MSJ = "Presione una tecla para continuar..."

opt = 1

def pokerFunc(cartas):
    esPoker = False

    numList = cartas.split()
    
    for i in numList:
        if numList.count(i) == 4:
            esPoker = True
            break
    
    return esPoker

def asignDatos(vec1, vec2):
    dataList = vec1.split()

    if len(dataList) > 3 or len(dataList) < 2:
        return print("Un vector está conformado mínimo por 2 componentes y máximo por 3")
    elif len(dataList) == 2:
        vec1_comp_i = float(dataList[0])
        vec1_comp_j = float(dataList[1])

        dataList.clear()

        dataList = vec2.split()

        vec2_comp_i = float(dataList[0])
        vec2_comp_j = float(dataList[1])

        vecList = [vec1_comp_i, vec1_comp_j, vec2_comp_i, vec2_comp_j]

        return vecList
    else:
        vec1_comp_i = float(dataList[0])
        vec1_comp_j = float(dataList[1])
        vec1_comp_k = float(dataList[2])

        dataList.clear()

        dataList = vec2.split()

        vec2_comp_i = float(dataList[0])
        vec2_comp_j = float(dataList[1])
        vec2_comp_k = float(dataList[2])

        vecList = [vec1_comp_i, vec1_comp_j, vec1_comp_k, vec2_comp_i, vec2_comp_j, vec2_comp_k]

        return vecList

def asignDatoUnico(vec1):
    dataList = vec1.split()

    if len(dataList) > 3 or len(dataList) < 2:
        return print("Un vector está conformado mínimo por 2 componentes y máximo por 3")
    elif len(dataList) == 2:
        vec1_comp_i = float(dataList[0])
        vec1_comp_j = float(dataList[1])

        vecList = [vec1_comp_i, vec1_comp_j]

        return vecList
    else:
        vec1_comp_i = float(dataList[0])
        vec1_comp_j = float(dataList[1])
        vec1_comp_k = float(dataList[2])

        vecList = [vec1_comp_i, vec1_comp_j, vec1_comp_k]

        return vecList

def prodPunto(vec1, vec2):
    
    elementosLista = asignDatos(vec1, vec2)
    if isinstance(elementosLista, list):
        if len(elementosLista) == 4:
            return elementosLista[0] * elementosLista[2] + elementosLista[1] * elementosLista[3]
        elif len(elementosLista) == 6:
            return elementosLista[0] * elementosLista[3] + elementosLista[1] * elementosLista[4] + elementosLista[2] * elementosLista[5]
    else:
        return "Vectores no válidos"

def ortogonal(vec1, vec2):
    
    if prodPunto(vec1, vec2) == 0:
        return "Los vectores: ", vec1, " y ", vec2, " SI son ortogonales"
    else:
        return "Los vectores: ", vec1, " y ", vec2, " NO son ortogonales"

def paralelo(vec1, vec2):

    elementosLista = asignDatos(vec1, vec2)

    if isinstance(elementosLista, list):
        if len(elementosLista) == 4:
            if elementosLista[0] / elementosLista[2] == elementosLista[1] / elementosLista[3]:
                return print("Los vectores: ", vec1, " y ", vec2, " SI son paralelos")
            else:
                return print("Los vectores: ", vec1, " y ", vec2, " NO son paralelos")
        elif len(elementosLista) == 6:
            if elementosLista[0] / elementosLista[3] == elementosLista[1] / elementosLista[4] == elementosLista[2] / elementosLista[5]:
                return print("Los vectores: ", vec1, " y ", vec2, " SI son paralelos")
            else:
                return print("Los vectores: ", vec1, " y ", vec2, " NO son paralelos")
    else:
        return "Vectores no válidos"

def normaVec():
    vec1 = input("Ingrese las componentes del vector 1\n")
    
    elementosLista = asignDatoUnico(vec1)
    if isinstance(elementosLista, list):
        if len(elementosLista) == 2:
            return sqrt(elementosLista[0]**2 + elementosLista[1]**2)
        elif len(elementosLista) == 3:
            return sqrt(elementosLista[0]**2 + elementosLista[1]**2 + elementosLista[2]**2)
    else:
        return "Vector no válido"

def listas(num):
    iguales = []
    mayores = []
    menores = []
    multiplos = []
    conjunto = []

    for i in range(0, 10):
        conjunto.append(randint(-20, 20))
    
    for i in conjunto:
        if num > float(i):
            menores.append(i)
        if num < float(i):
            mayores.append(i)
        if num == float(i):
            iguales.append(i)
        if i == 0:
            continue
        elif num % float(i) == 0:
            multiplos.append(i)

    return print("Lista:", conjunto, "\nMayores:", mayores, "\nMenores: ", menores, "\nIguales: ", iguales, "\nMultiplos: ", multiplos)

while opt == 1:
    sel = int(input("1. Representación barajas con tuplas\n2. Poker\n3. Prod escalar\n4. Ortogonal\n"
                    "5. Paralelo\n6. Norma\n7. Devolver listas\n8. Salir\n"))

    if sel == 1:
        negrasPicas = ((1,2,3,4,5,6,7,8,9,10),"J","K","Q")
        rojasCorazones = ((1,2,3,4,5,6,7,8,9,10),"J","K","Q")
        negrasTreboles = ((1,2,3,4,5,6,7,8,9,10),"J","K","Q")
        rojasDiamantes = ((1,2,3,4,5,6,7,8,9,10),"J","K","Q")

        print("Negras Picas: ", negrasPicas,
                "\nRojas Corazones: ", rojasCorazones,
                "\nNegras Treboles: ", negrasTreboles,
                "\nRojas Diamantes: ", rojasDiamantes)

        print(MSJ)
        msvcrt.getch()

    if sel == 2:
        cartas = input("Introduzca los números de las cartas separados por un espacio:\n")
        
        if pokerFunc(cartas):
            print("¡Poker!")
        else:
            print("No es poker...")

        print(MSJ)
        msvcrt.getch()

    if sel == 3:
        vec1 = input("Ingrese las componentes del vector 1\n")
        vec2 = input("Ingrese las componentes del vector 2\n")
        result = prodPunto(vec1, vec2)

        print("Producto punto entre el vector: ", vec1, " y el vector: ", vec2, " es = ", result)

        print(MSJ)
        msvcrt.getch()

    if sel == 4:
        vec1 = input("Ingrese las componentes del vector 1\n")
        vec2 = input("Ingrese las componentes del vector 2\n")
        print(ortogonal(vec1, vec2))

        print(MSJ)
        msvcrt.getch()
    
    if sel == 5:
        vec1 = input("Ingrese las componentes del vector 1\n")
        vec2 = input("Ingrese las componentes del vector 2\n")
        
        paralelo(vec1, vec2)

        print(MSJ)
        msvcrt.getch()
    
    if sel == 6:
        result = normaVec()
        print("La norma del vector es", result)

        print(MSJ)
        msvcrt.getch()

    if sel == 7:
        num = int(input("Ingrese número para evaluar: \n"))
        listas(num)

        print(MSJ)
        msvcrt.getch()
    if sel == 8:
        opt += 1