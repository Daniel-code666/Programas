import pyodbc
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                        'Server=LAPTOP-UJGB0AUP;'
                        'Database=Mercado;'
                        'UID=usuarioSQL;'
                        'PWD=123;')

class producto:    
    def Get(self):
        cursor = conn.cursor()    
        cursor.execute('select * from Producto')

        for row in cursor:
            print(row)

    def Create(self, name, prec):
        try:
            cursor = conn.cursor()
            query = ('insert into Producto(nombre, precio) values(?,?)')
            cursor.execute(query, [name, prec])
            cursor.commit()
        except Exception:
            print(Exception)

    def Updt(self, index):
        opt = 1

        cursor = conn.cursor()
        query = ('select * from Producto where id = ?')
        cursor.execute(query, [index])

        for row in cursor:
            print(row)

        while opt == 1:
            try:
                sel = int(input("1. Cambiar nombre\n2. Cambiar precio\n3.Regresar\n"))

                if sel == 1:
                    name = input("Ingrese nuevo nombre:\n")
                    
                    cursor = conn.cursor()
                    query = ('update producto set nombre = ? where id = ?')
                    cursor.execute(query, [name, index])
                    cursor.commit()
                    print("Nombre actualizado")

                if sel == 2:
                    prec = float(input("Ingrese nuevo precio: \n"))

                    cursor = conn.cursor()
                    query = ('update producto set precio = ? where id = ?')
                    cursor.execute(query, [prec, index])
                    cursor.commit()
                    print("Precio actualizado...")

                if sel == 3:
                    opt += 1

            except ValueError:
                print("Debe ingresar valores válidos...")

    def Delete(self, index):
        cursor = conn.cursor()
        query = ('select * from Producto where id = ?')
        cursor.execute(query, [index])

        for row in cursor:
            print(row)

        try:
            sel = int(input("¿Desea eliminar el producto elegido? SI:1 NO:0\n"))

            if sel == 1:
                cursor = conn.cursor()
                query = ('delete from Producto where id = ?')
                cursor.execute(query, [index])
                cursor.commit()
                print("Producto eliminado")
            else:
                return print("Operación cancelada")
        except ValueError:
            print("Debe ingresar un valor válido")
