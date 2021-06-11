"""
    #-------------------------------------------------------------------------------
    #
    # Nombre:			Sesion11_Cadenas_f.py
    # Proposito:		Explicar las funcionalidades de las cadenas formateadas con f
    #
    # Autor:			Omar Vargas
    #
    # Creado:			20/05/2021
    #
    #-------------------------------------------------------------------------------
"""

#Dar formato a un print - los simbolos {} son operadores de posición
a=5
b=3
c=2
print(a,b)
#print(a+"es igual a"+b) #3 es igual a 5
print(a,"es igual a",b)
print("{} es igual a {} y otro {}".format(b,c,a))  
print(f"{a} es igual a {b}")

texto = f"{a} es igual a {b}"
type(texto)


# Una cadena "f" se suele presentar como un literal 
# entrecomillado al que le precede el carácter "f" o "F"
f'cadena'

# El resultado de evaluar una cadena "f" 
# se puede asignar a una variable
cadenaf=f'cadena'

# También, se puede extender a varias líneas 
# utilizando las triples comillas
cadenaf= f'''Este es un texto
mostrado entre
varias lineas'''
print(cadenaf)

# Dentro de una cadena "f" se pueden insertar variables
# y expresiones escribiéndolas entre llaves {}
modelo='Alma'
precio=650
impuestos=precio*21/100
p = precio+impuestos
print(p)
print(f'Bicicleta {modelo}: {precio + impuestos} euros')

# A partir de Python 3.8 un signo igual '=' tras el nombre de una variable 
# inserta tanto el nombre de la variable como su valor
importe=1300
descuento=15
print(f'Información de la compra: {importe=} €, {descuento=} %')
#Información de la compra: importe=1300 €, descuento=15 %

# Las dobles llaves se utilizan para expresar el nombre de una variable 
# o mostrar literalmente una expresión y no su valor
nombre='Claudia'
cadena=f'La variable {{nombre}} contiene {nombre}' 
print(cadena) #La variable {nombre} contiene Claudia

# Una expresión de una cadena "f" puede incluir llamadas a funciones
def suma(a,b):
    return a+b

a=10
b=a*12  
resp=f'La suma total es {suma(a,b)}'
print(resp)

# ...Y la función Lambda es una función más:
b=10
h=5
print(f'Área triángulo: {(lambda b,h: b*h/2)(b,h)}')

# Podemos usar las cadenas "f" para rellenar un texto
titulo='Fundamentos Python'
print(f'{titulo:_^30}')  # ______Fundamentos Python______
print(f'{titulo:_<30}')  # Fundamentos Python____________ 
print(f'{titulo:_>30}')  # ____________Fundamentos Python

# Podemos usar este mismo rellenado para alinear un resultado
lista=[2000, 500, 17000, 24, 7]
for elemento in lista:
    #disponemos entre llaves la variable seguida de (:) y la cantidad de espacios que ocupará la variable
    print(f"{elemento:10}")
print("----------")    
print(f"{sum(lista):10}")

#Podemos usar las cadenas f para dar formato a un número con X cantidad de decimales
lista=[30.195, 400.2, 20.5555, 18.34732, 67]
for elemento in lista:
    print(f"{elemento:.2f}")
#Podemos combinar el alineado con el formato de decimales
lista=[30.195, 400.2, 20.5555, 18.34732, 67]
for elemento in lista:
    print(f"{elemento:10.2f}")
#O mostrar varios elementos formateados con diferente cantidad de decimales
lista=[30.195, 400.2, 20.5555, 18.34732, 67]
for elemento in lista:
    print(f"{elemento:10.2f} {elemento:10.3f}")



#Pluss -- split(sep=None, maxsplit=1)
a = "Hola mundo"
b= a.split()
print(b)

a = input().split()
print(a[0])