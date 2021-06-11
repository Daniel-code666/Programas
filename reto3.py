
vacunasList = []

cantPer = int(input())

for i in range(0, cantPer):
    infoPersona = input()
    infoList = infoPersona.split()

    edad = infoList[0]
    hemoglobina = infoList[1]
    masa_corp = infoList[2]
    tension_sist = infoList[3]
    tension_dias = infoList[4]

    if int(edad) >= 80 and int(hemoglobina) > 7 and int(masa_corp) > 30 and int(tension_sist) >= 140 and int(tension_dias) >= 90:
        vacunasList.append(edad)

if not vacunasList:
    print("NO DISPONIBLE")
else:
    for i in vacunasList:
        print(i)