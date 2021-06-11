numero_magico = []

num_mag = input("Escriba 12345679: ")

if num_mag == '12345679':
    print(num_mag)
else:
    print(num_mag.replace('8',''))
    num_mag2 = num_mag.replace('8','')
    print(num_mag2)

# for i in range(1,10):
#     elem = int(input("Ingrese los números: "))
#     if elem == 8:
#         continue
#     else:
#         numero_magico.append(elem)

# numero_usuario = int(input("Ingrese un número de 1 a 9: "))

# if numero_usuario < 0 and numero_usuario > 10:
#     print("Ingrese un número con respecto al rango")
#     numero_usuario = int(input("Ingrese un número de 1 a 9: "))
# else:


#print(numero_magico)
