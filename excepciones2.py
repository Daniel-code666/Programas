from random import randint

opt, cont = 1, 0

lista = []

for i in range(0, 10):
    num = randint(1, 20)
    
    if num not in lista:
        lista.append(num)

print(lista)

while True:
    numUser = int(input("Ingrese un número, para salir ingrse un 0:\n"))
    try:
        if numUser == 0:
            break
        if numUser is None:
            raise ValueError
        if numUser in lista:
            raise TypeError
        else:
            cont += 1
            lista.append(numUser)
    except ValueError:
        print("Debe seguir ingresando valores o ingrese 0 para salir")
    except TypeError:
        print("El número ingresado ya está en la lista")

print(lista[:10], "\n",lista[-cont:])