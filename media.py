sumNum = 0

num = input("Ingrese los números separados por un espacio\nej: 1 2 3 4\n")

numList = num.split()

for i in range(0, len(numList)):
    sumNum += int(numList[i])

prom = sumNum / len(numList)

print("Media: ", prom)