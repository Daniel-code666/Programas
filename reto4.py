infoInic = input()

billetes = input()

infoList = infoInic.split()

billetesList = billetes.split()

tempDict = {}
tempDictReversed = {}

cont, cont2 = 0, 0

for i in billetesList:
    if i not in tempDict and billetesList.count(i) >= 2:
        tempDict[i] = billetesList.count(i)
        cont += 1

newList = list(reversed(billetesList))

lim = int(infoList[1])



print(sum(tempDict.values()) - cont, cont2)