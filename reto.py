datos = input()

dataList = datos.split()

salario = float(dataList[0])
hrsExtra = float(dataList[1])
bonus = float(dataList[2])

bono = 0
hrExtra = 0

valHrTrab = salario / 187

if hrsExtra > 0:
    hrExtra = valHrTrab * 1.39
    hrExtra *= hrsExtra

if bonus > 0:
    bono = salario * 0.066

totSalNoDesc = salario + hrExtra + bono

salud = totSalNoDesc * 0.05
pension = totSalNoDesc * 0.02
compensacion = totSalNoDesc * 0.01

totSalSiDesc = totSalNoDesc - salud - pension - compensacion

dataList[0] = totSalSiDesc
dataList[1] = totSalNoDesc

print("{0:.1f}".format(dataList[1]), "{0:.1f}".format(dataList[0]))