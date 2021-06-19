import os

archivo = open('prod.txt', 'w')

archivo.write('DROGERIA Y MEDS - ASPIRINA X 35 - 30500\n')

arch = r"C:\Users\Daniel\Desktop\Trabajos\Fundamentos con Python\Docs\requerimientos_ejer1.txt"

if os.path.exists(arch):
    print(True)
    for i in arch:
        print(arch.read())
    archivo.close()