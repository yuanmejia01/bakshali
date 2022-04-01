#Aproximar una raiz
from math import *
from termcolor import cprint
class Bakshali:
    def __init__(self, S):
        self.S = S
    def bakshali(self, x_0):
        a_n = (self.S - pow(x_0,2))/(2*x_0)
        b_n = x_0 + a_n
        x_n = b_n -(a_n/(2*b_n))
        #Resultado de una iteracion
        return x_n
"""    def iteraciones(self, iteraciones):
        for i in range(iteraciones):
            x_n = Bakshali.bakshali(self,)

        return x_n #Despues de iteraciones"""

def main():
    S = int(input("Ingrese el radicando S: "))
    x0 = int(input("Ingrese la aproximacion inicial x0: "))
    iteraciones = int(input("Ingrese el numero de iteraciones que desea realizar: "))

    aproximaciones = []
    aproximaciones.append(x0)
    bakshali = Bakshali(S)

    for i in range(iteraciones):
        x_n = bakshali.bakshali(aproximaciones[-1])
        aproximaciones.append(x_n)

    cprint(f"El resultado de la raiz cuadrada de {S} por el metodo de Bakshali, tras {iteraciones} y con una aproximacion inicial de {x0}, es {aproximaciones[-1]}","yellow")

main()