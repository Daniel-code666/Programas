"""
    #-------------------------------------------------------------------------------
    #
    # Nombre:			Sesion23_Persistencia1.py
    # Proposito:		Explicar los conceptos para mantener la persistencia de datos 
    #                   en python 
    #
    # Autor:			Omar Vargas
    #
    # Creado:			06/06/2021
    #
    #-------------------------------------------------------------------------------
"""

"""
    La función open() abre un archivo y lo devuelve como un objeto de archivo
    
    SINTAXIS:
    open(file, mode)
        file = Ruta y nombre del archivo
        mode = Modo de apertura
            'r' - Read - Valor predeterminado. Abre un archivo para lectura, error si el archivo no existe
            'a' - Append - Abre un archivo para agregar, crea el archivo si no existe
            'w' - Write - Abre un archivo para escritura, crea el archivo si no existe
            'x' - Create - Crea el archivo especificado, devuelve un error si el archivo existe
        
        Además, puede especificar si el archivo debe manejarse en modo binario o de texto
            't' - Text  - Valor predeterminado. Modo texto
            'b' - Binary - Modo binario (p. ej., imágenes)

    METODOS:
    .read()  - Leer todo el contenido de un archivo
    .readline()  - Lee una línea del archivo, si llega al final del archivo retorna un string vacio ("")
    .readlines() - Lee todas las líneas de un archivo y las almacena en una lista
    .write() - Escribir en un archivo
    .writelines() - Escribe una lista de elementos dados, uno por linea
    .close() - Cerrar archivo
"""

#-------------------------------------CREAR ARCHIVO VACIO----------------------------------------#
#Paso 1: Crear archivo
archivo = open('Productos.txt','x') 


#------------------------ABRIR ARCHIVO EN MODO ESCRITURA (Sobreescribir)----------------------#

"""METODO 1"""
#Paso 1: Abrir el archivo en modo escritura
archivo = open('Productos.txt','w') 

#Paso 2: Escribir sobre el archivo 3 lineas nuevas
archivo.write('DROGUERIA Y MEDICAMENTOS - ASPIRINA EFERVESCENTE X 50 - 30500\n')
archivo.write('DROGUERIA Y MEDICAMENTOS - BONFIEST PLUS X 16 - 32500\n')
archivo.write('DROGUERIA Y MEDICAMENTOS - NOXPIRIN DIA Y NOCHE X 24 - 24000\n')

#Paso 3: Cerrar el archivo
archivo.close()

"""METODO 2"""
#Paso 1: Abrir el archivo en modo escritura
archivo = open('Productos.txt','w') 

#Paso 2: Recibir los elementos a ingresar en modo lista
elementos = ['DROGUERIA Y MEDICAMENTOS - ASPIRINA EFERVESCENTE X 50 - 30500\n', 'DROGUERIA Y MEDICAMENTOS - BONFIEST PLUS X 16 - 32500\n', \
    'DROGUERIA Y MEDICAMENTOS - NOXPIRIN DIA Y NOCHE X 24 - 24000\n']

#Paso 3: Escribir sobre el archivo
archivo.writelines(elementos)

#Paso 4: Cerrar el archivo
archivo.close()


#------------------------------ABRIR ARCHIVO EN MODO LECTURA------------------------------#

"""METODO 1 - Leer cada linea"""
#Paso 1: Abrir el archivo en modo lectura
archivo = open('Productos.txt','r') 

#Paso 2: Leer los datos del archivo
for linea in archivo:
    print(linea)

#Paso 3: Cerrar el archivo
archivo.close()

"""METODO 2 - Leer todo el archivo"""
#Paso 1: Abrir el archivo en modo lectura
archivo = open('Productos.txt','r') 

#Paso 2: Leer los datos del archivo
print(archivo.read())

#Paso 3: Cerrar el archivo
archivo.close()


#-----------------------ABRIR ARCHIVO EN MODO ESCRITURA (Actualizar)-----------------------#
#Paso 1: Abrir el archivo en modo escritura
archivo = open('Productos.txt','a') 

#Paso 2: Escribir sobre el archivo 3 lineas nuevas
archivo.write('MISCELANIA - MICROPUNTAS DORICOLOR SURTIDO X 12 - 7800\n')
archivo.write('MISCELANIA - RESALTADOR PELIKAN SUR/COL X 10 - 9000\n')
archivo.write('MISCELANIA - SILIKONA GRUESA Y DELGADA X KILO - 13000\n')

#Paso 3: Cerrar el archivo
archivo.close()


#----------------------------LECTURA LINEA A LINEA DE UN ARCHIVO----------------------------#
#Paso 1: Abrir el archivo en modo lecura
archivo = open('Productos.txt','r') 

#Paso 2: Leer cada linea del archivo
linea = archivo.readline()
while linea != '':
    print(linea)
    linea = archivo.readline()

#Paso 3: Cerrar el archivo
archivo.close()


#----------------------------LECTURA DE UN ARCHIVO Y DEVOLVER LISTA----------------------------#
#Paso 1: Abrir el archivo en modo lecura
archivo = open('Productos.txt','r') 

#Paso 2: Leer todas las lineas del archivo
lineas = archivo.readlines()
print(lineas)

#Paso 3: Cerrar el archivo
archivo.close()


#-----------------------------------ELIMINAR SALTOS DE LINEA------------------------------------#
#Paso 1: Abrir el archivo en modo lecura
archivo = open('Productos.txt','r') 

#Paso 2: Leer los datos del archivo sin saltos de linea
for linea in archivo:
    if linea[-1] == '\n':
        linea = linea[:-1] #Desde el inicio de la linea hasta su posicion final-1
    print(linea)

#Paso 3: Cerrar el archivo
archivo.close()


#--------------------------MANEJO DE ERRORES DE APERTURA DE ARCHIVOS---------------------------#
#Si trata de abrir en modo lectura un archivo inexistente, se obtiene un error y la ejecución del programa se aborta.
#Para evitar esto tenemos dos opciones:

#1. Preguntar si el archivo existe
import os
archivo = r"C:\Test\test.txt" #Cadena r, permite mostrar la cadena cruda sin tener presente los caracteres de escape
print(os.path.isfile(archivo)) #Este método nos permite validar si un archivo existe o no

if os.path.isfile(archivo) == False:
    print('El archivo no se encuentra en la ruta')
else:
    archivo = open(r'C:\Test\test.txt','r') 
    for linea in archivo:
        print(archivo.read())
    archivo.close()

#2. Capturar la excepción de la apertura
def valida_existencia(filePath):
    try:
        archivo = open(filePath,'r') 
        with archivo as f: #la sentencia with permite abrir el archivo y despues cerrarlo sin necesidad de especificar .close()
            for linea in archivo:
                print(archivo.read())
        return True
    except FileNotFoundError as e: #(en Python 3.x)
        print('El archivo no se encuentra en la ruta')
        return False
    except IOError as e: #(en Python 2.x) 
        print('El archivo no se encuentra en la ruta')
        return False

archivo = r'C:\Test\test.txt'
valida_existencia(archivo)

#--------------------------------EJEMPLO PRACTICO---------------------------------#
"""
    Desarrollar un programa que calcule el número de líneas de un archivo de texto.
"""
#Paso 1: Abrir el archivo en modo lecura
archivo = open('Productos.txt','r') 

#Paso 2: Definir contador
contador = 0

#Paso 3: Leer cada linea del archivo y validar si esta vacia; 
#en caso contrario contar la linea y leer la siguiente linea
linea = archivo.readline()
while linea != '' :
    contador += 1
    linea = archivo.readline()

#Paso 4: Cerrar el archivo
archivo.close()

#Paso 5: Indicar cuantas lineas tiene el archivo
print(f'El archivo leido tiene {contador} lineas')

#--------------------------------EJERCICIOS DE CLASE---------------------------------#
"""
    1. Diseña un programa que cuente el número de caracteres de un archivo de texto, incluyendo los saltos de línea.
        (Nota: El archivo debe estar ubicado en la carpeta raiz)

    2. Diseñe una función que, reciba una palabra y un nombre de archivo y diga si la palabra aparece o no en el archivo.
        (Validar que se encuentre el archivo)
    
    3. Diseñe una función que, reciba un nombre de archivo y muestre cada una de sus líneas precedida por su numero de línea.
        (Validar que se encuentre el archivo)
"""