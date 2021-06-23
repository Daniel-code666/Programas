infoInic = input()

billetes = input()

infoList = infoInic.split()

billetesList = billetes.split()

tempDict = {}

cont, cont2 = 0, 0

for i in billetesList:
    if i not in tempDict and billetesList.count(i) >= 2:
        tempDict[i] = billetesList.count(i)
        cont += 1

inic = 1
end = int(infoList[1]) + 1

for i in range(len(billetesList) - 1):
    for j in range(inic, len(billetesList[:end])):    
        if billetesList[i] == billetesList[j]:
            cont2 += 1
            inic += 1
            end += 1

    if end == len(billetesList) + 1 or cont2 == 0:
        break

print(sum(tempDict.values()) - cont, cont2)