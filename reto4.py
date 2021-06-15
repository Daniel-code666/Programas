infoInic = input()

billetes = input()

infoList = infoInic.split()

billetesList = billetes.split()

tempDict = {}

cont = 0

for i in billetesList:
    if i not in tempDict and billetesList.count(i) >= 2:
        tempDict[i] = billetesList.count(i)
        cont += 1


print(sum(tempDict.values()) - cont)