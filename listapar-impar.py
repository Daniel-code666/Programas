numString = input("Ingrese los números separados por espacios\n")

numList = numString.split()

numPar, numImpar = [], []

for i in range(1, len(numList)):
    if int(numList[i]) % 2 == 0:
        numPar.append(numList[i])
    else:
        numImpar.append(numList[i])

print(numPar, "\n", numImpar)