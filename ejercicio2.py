numero_magico = 12345679

numero_usuario = int(input())

if numero_usuario < 0 or numero_usuario > 9:
    print("Ingrese un número con respecto al rango")
else:
    numero_usuario *= 9
    numero_magico *= numero_usuario
    print("Valor del número mágico {}".format(numero_magico)) 

# opt = 1

# try:
#     numero_usuario = int(input("Ingrese un número de 1 a 9, ¡si ingresa una letra el programa explota!: "))
#     while opt == 1:
#         if numero_usuario < 0 or numero_usuario > 9:
#             print("Ingrese un número con respecto al rango")
#             numero_usuario = int(input("Ingrese un número de 1 a 9: "))
#         else:
#             opt += 1

#     numero_usuario *= 9
#     numero_magico *= numero_usuario
#     print("Valor del número mágico {}".format(numero_magico))
# except ValueError:
#     print("Debió de haber ingresado un número *el programa explota...")

