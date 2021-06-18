
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

tempList = []
newnewList = []

end = int(infoList[1])

for i in newList[1:end + 1]:
    orig = newList[0]

    if i == orig or i in tempDict:
        newnewList.append(int(i))

    if int(i) in newnewList and i in tempDict:
        cont2 += 1 



print(sum(tempDict.values()) - cont, sum(tempDict.values()) - cont2)