"""
    #-------------------------------------------------------------------------------
    #
    # Nombre:			Sesion5_UsergioA.py
    # Proposito:		En este programa se explicararán los conceptos mensionados en la
    #                   Sesion 5: Realización de operaciones aritméticas y lógicas en programación
    #
    # Autor:			Omar Vargas
    #
    # Creado:			11/05/2021
    #
    #-------------------------------------------------------------------------------
"""

#Extensiones recomendadas
#Bracket Pair Colorizer (Asigna un color a una sección de código para poder identificarla más fácil)
#indent-rainbow (Colorea la identación de mi codigo)
#Project Manager (Agraga una pestaña para trabajar con varios proyectos)
#Python Docstring Generator (Automatiza la generación de Docstring)

#Tipos de datos en Python
#Documentación Tipos de Datos -- https://docs.python.org/3/library/datatypes.html


int() #Dato tipoentero
variable = 5
type(variable)

float() #Dato tipo flotante
variable = 5.3
type(variable)

complex() #Dato tipo complejo
variable = 5j
type(variable)

str() #Dato tipo string
variable = "23"
variable2 = '5'
type(variable)

bool() #Dato tipo booleano
variable = True
variable = False
type(variable)

list() #Dato tipo lista -- Secuencia ordenada de elementos
variable = [1, 2.2, 'python']
type(variable)
variable[0] # Operador de slicing
print (variable[2])
#Opciones de generar una lista vacia
Lista_Vacia = list()
Lista_Vacia = []

tuple() #Dato tipo tupla -- Secuencia ordenada "inmutable" de elementos
variable = (5,'program', 1+3j)
type(variable)

dict() #Dato tipo diccionario -- Colleción no-ordenada de pares llave-valor
variable = {"Llave1":'valor de la llave 1','Llave2': "valor de la llave 2"}
variable = {"Llave1":0,'Llave2': 2}
type(variable)
print (variable["Llave2"])
#Opciones de generar una dicionario vacio
Dict_Vacio = dict()
Dict_Vacio = {}

set() #Dato tipo set (Conjunto) -- Secuencia no-ordendada de elementos
variable = {5,2,3,1,4}
type(variable)
#No acepta elementos repetidos
variable = {5,2,3,1,1,2,3,4,4}
print (variable)
#Podemos realizar operaciones entre conjuntos de unión (|) , diferencia (-), intersección (&) y diferencia simétrica (^)


#1. Operadores aritméticos
#Suma +
suma = 4 + 5
print (suma)
#Resta - 
resta = 8 - 3
print (resta)
#Multiplicacion *
multiplica = 5 * 8
print (multiplica)
#División de dos valores /
divide = 7 / 2
print (divide)
#División entera de dos valores //
divideentero = 6.5 // 2
print (divideentero)
#Módulo % - El cociente de la división de dos números que deben ser enteros
modulo = 7 % 2
print (modulo)

#2. Operadores asignación
#Asignación =
variable = 5
#Asignación con suma +=
suma += 5
print(suma)
#Asignación con resta -=
resta -= 3
print(resta)
#Asignación con multiplicación *=
multiplica *= 8
print(multiplica)
#Asignación con división /=
divide /= 5
#Asignación con división entera //=
divideentero //= 3
#Asignación con módulo %=
modulo %= 2

#3. Conversión de tipos de datos numéricos
#De entero a real: si se realiza una operación entre un numero real y un numero entero, en la operación se asigna un .0 al resultado de la operación --- Conversion Implicita
operacion = 2 + 1.6
print (operacion)

#De real a entero: dado un dato o una variable de tipo real se aplica la función int() --- Conversion Explicita
conversion = int(1.0)
print (conversion)

dato1 = int(input("Ingrese un número: "))
type(dato1)


#4. Operadores lógicos
a = True
b = False
#not: negación: not(var)
print(not(a))
#and: conjunción: var1 and var2
print(a and b)
#or: disyunción: var1 or var2
print(a or b)

#5. Operadores de igualdad
a = 3
b = 5
#== devuelve verdadero si dos valores son iguales
print(a == b)
#!= devuelve verdadero si dos valores son diferentes
print(a != b)
#> mayor que, devuelve verdadero si el primero operador es estrictamente mayor que el segundo operador
print(a > b)
#< menor que, devuelve verdadero si el primero operador es estrictamente menos que el segundo operador
print(a < b)
#>= mayo o igual
print(a >= b)
#<= menor o igual
print(a <= b)

#6. Estructuras de Control
#Si entonces if else
a = 3
b = 5
if a > b:
    print(a," es mayor que ",b)
elif a < b:
    print(a," es menor que ",b)
else:
    #print(a,"no es mayor",b)
    print("{} es igual a {}".format(a,b))

#mientras que -- while
while a < 5:
    print(a)
    a += 1

