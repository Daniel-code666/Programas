
resultList = []

datos = input()

datosList = datos.split()

distCamaras = float(datosList[0])
actRecord = float(datosList[1])
tiempo = float(datosList[2])

vel = distCamaras / tiempo

vel *= 3.6

resultList.append(round(vel,1))

if distCamaras < 0 or actRecord < 0 or tiempo < 0:
    print("ERROR")
else:
    if vel > (actRecord * 0.20) + actRecord:
        resultList.append("ENTREVISTA")
        print(resultList[0], resultList[1])
    elif vel > actRecord:
        resultList.append("NUEVO RECORD")
        print(resultList[0], resultList[1])
    else:
        resultList.append("VELOCIDAD NORMAL")
        print(resultList[0], resultList[1])
