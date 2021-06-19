import pyodbc
import producto
import msvcrt

MSJ = "Presione una tecla para continuar..."


opt = 1

prod = producto.producto()

while opt == 1:
    sel = int(input("1. Ver lista de productos\n2. Crear producto\n3. Editar producto\n4. Eliminar producto"
                    "\n5. Salir\n"))

    if sel == 1:
        prod.Get()
        print(MSJ)
        msvcrt.getch()

    if sel == 2:
        try:
            name = input("Ingrese nombre del producto:\n")
            prec = float(input("Ingrese precio del producto:\n"))
            prod.Create(name, prec)

        except ValueError:
            print("Debe ingresar valores válidos")
        print(MSJ)
        msvcrt.getch()

    if sel == 3:
        try:
            index = int(input("Ingrese el índice del producto a modificar:\n"))
            prod.Updt(index)
        except ValueError:
            print("Debe ingresar un vlaor válido")
        print(MSJ)
        msvcrt.getch()

    if sel == 4:
        try:
            index = int(input("Ingrese el índice del producto a eliminar:\n"))
            prod.Delete(index)
        except ValueError:
            print("Debe ingresar un valor válido")
        print(MSJ)
        msvcrt.getch()


    if sel == 5:
        opt += 1    

