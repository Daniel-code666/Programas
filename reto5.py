
productos = {1:['Mango',7000.0,99],
            2:['Limones',3600.0,95],
            3:['Peras',2700.0,85],
            4:['Arandanos',8300.0,74],
            5:['Tomates',8100.0,44],
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
        productos[int(infoList[0])] = [infoList[1], float(infoList[2]), infoList[3]]
        precioMax()

def updt(info):
    infoList = info.split()

    tempDict = {int(infoList[0]):[infoList[1],float(infoList[2]),infoList[3]]}

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
    maxValor = 0
    minValor = 99999
    precList= []
    contador = 0
    multi = 0
    cont = 0
    for i in productos.values():
        for j in i:
            if type(j) == float:
                precList.append(j)
                contador += 1
                multi = j * float(i[2])
                cont += multi
                if maxValor < j:
                    maxValor = j
                    maxProducto = i[0]
                if minValor > j:
                    minValor = j
                    minProducto = i[0]
    return print(maxProducto, minProducto, round((sum(precList)/contador), 1), round(cont,1))

cadena = input()
info = input()

if cadena == "AGREGAR":
    add(info)

if cadena == "ACTUALIZAR":
    updt(info)

if cadena == "BORRAR":
    delete(info)

if cadena == "max":
    precioMax()
