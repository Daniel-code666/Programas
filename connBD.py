import pyodbc

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                        'Server=LAPTOP-UJGB0AUP;'
                        'Database=Mercado;'
                        'UID=usuarioSQL;'
                        'PWD=123;')

cursor = conn.cursor()
cursor.execute('select * from Producto')

for row in cursor:
    print(row)

