# Se requiere crear un menú para un cajero automático que me permita moverme entre las diferentes opciones del menú 
# y continúe solicitando opciones hasta que le indique que deseo salir del sistema.

# Las opciones que tendrá el menú son las siguientes:

# Consulta de Saldo
# Retiro
# Depósito
# Salir

opt, tot, ret, depo = 1, 0, 0, 0

while opt == 1:
    print("Bienvenido a 'Cajero en el Bolsillo' ver1.0")
    print("1. Consultar saldo '\n'2. Hacer un retiro '\n'3. Depositar '\n'4. Salir")
    sel = int(input("¿Qué desea hacer? Digite el número de acuerdo a la opción que desea usar: "))
    
    if sel == 1:
        print("Consultar saldo")
        print("El saldo actual es de: ", tot)
    
    if sel == 2:
        print("Hacer un retiro")
        print("Saldo actual: ", tot)
        ret = float(input("Ingrese cantidad del retiro: "))

        if tot == 0 or ret > tot or ret == 0:
            print("No puede hacer esa operación debido a que el saldo actual es igual a 0 o el valor del retiro es mayor del saldo actual")
        else:
            tot -= ret
            print("Saldo actual: ", tot)
    
    if sel == 3:
        print("Depositar")
        depo = float(input("Ingrese cantidad de deposito: "))

        tot += depo
        print("Saldo actual", tot)

    if sel == 4:
        print("Saliendo...")
        opt += 1