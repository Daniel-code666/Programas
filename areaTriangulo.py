import math

opt = 1

ladoA = int(input("Ingrese valor del lado A: "))
ladoB = int(input("Ingrese el valor del lado B: "))

hipo = math.sqrt(ladoA*ladoA + ladoB*ladoB)

print("El área del triángulo es: ", (ladoA*ladoB)/2)