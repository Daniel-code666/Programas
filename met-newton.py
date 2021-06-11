from sympy import symbols
from sympy.core.function import Derivative

x = symbols('x')

def ecuacionfunc(num):
    result = eval(expr).subs(x, num)
    return result

def derivFunc(num):
    exprDerivada = Derivative(expr, x)
    resultDerivada = exprDerivada.doit().subs({x:num})
    return resultDerivada

def newtonFunc(num):
    h = ecuacionfunc(num) / derivFunc(num)
    while abs(h) >= 0.0001:
        h = ecuacionfunc(num) / derivFunc(num)

        num += - h

    print("El valor de la raiz de la ecuación: ", expr, " es: ", num)

info = input("Ingrese la ecuación y el punto inicial separados por un espacio\nEj: x**3+2*x*2-5 4\n")

infoList = info.split()

expr = infoList[0]
numInic = float(infoList[1])

newtonFunc(numInic)

