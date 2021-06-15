productos = {1:['Mango',7000.0,99],
            2:['Limones',3600.0,95],
            3:['Peras',2700.0,85],
            4:['Arandanos',8300.0,74],
            5:['Tomates',8400.0,44],
            6:['Fresas',7100.0,99],
            7:['Helado',4400.0,98],
            8:['Galletas',400.0,99],
            9:['Chocolates',4500.0,90],
            10:['Jamon',17000.0,89]}

def add(info):
    infoList = info.split()

    if int(infoList[0]) in productos:
        return print("ERROR")
    else:
        productos[int(infoList[0])] = [infoList[1], float(infoList[2]), int(infoList[3])]
        precioMax()

def updt(info):
    infoList = info.split()

    tempDict = {int(infoList[0]):[infoList[1], float(infoList[2]), int(infoList[3])]}

    if int(infoList[0]) not in productos:
        return print("ERROR")
    else:
        productos.update(tempDict)
        precioMax()

def delete(info):
    infoList = info.split()

    if int(infoList[0]) not in productos:
        return print("ERROR")
    else:
        del productos[int(infoList[0])]
        precioMax()

def precioMax():
    tempListKeys = []
    tempListVal = []
    tempListCant = []
    listaProd = []

    for i in productos.values():
        for j in i:
            if type(j) == str:
                tempListKeys.append(j)
            if type(j) == float:
                tempListVal.append(j)
            if type(j) == int:
                tempListCant.append(j)
    
    for i, j in zip(tempListVal, tempListCant):
        listaProd.append(i * j)

    prom = sum(tempListVal) / len(tempListVal)
    zip_iter = zip(tempListKeys, tempListVal)
    tempDict = dict(zip_iter)

    return print(max(tempDict, key=tempDict.get), min(tempDict, key=tempDict.get), round(prom, 1), round(sum(listaProd), 1))

cadena = input()
info = input()

if cadena == "AGREGAR":
    add(info)

if cadena == "ACTUALIZAR":
    updt(info)

if cadena == "BORRAR":
    delete(info)
