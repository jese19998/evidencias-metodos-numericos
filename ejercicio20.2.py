#Equipo Jese Manuel Acosta Avila y Gabriela Ramirez Cortez
from mpl_toolkits.mplot3d import Axes3D
from sympy import * 
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x) * np.sin(x)

x = np.linspace(0, np.pi, 101)
plt.plot(x, f(x))
plt.grid()
plt.show()

def simpson13(n, a, b, f):

    h = (b - a) / n
   
    suma = 0.0



    for i in range(1, n):
        #calculamos la x
        #x = a - h + (2 * h * i)
        x = a + i * h
        # si es par se multiplica por 4
        if(i % 2 == 0):
            suma = suma + 2 * fx(x, f)
        #en caso contrario se multiplica por 2
        else:
            suma = suma + 4 * fx(x, f)
    #sumamos los el primer elemento y el ultimo
    suma = suma + fx(a, f) + fx(b, f)
    #Multiplicamos por h/3
    rest = suma * (h / 3)
    #Retornamos el resultado
    return (rest)

#Funcion que nos ayuda a evaluar las funciones
def fx(x, f):
    return eval(f)

#valores de ejemplo para la funcion sin(x) con intervalos de
n = 200
a = 0.1
b = 2.0
f = '2*x**3-5*x**2+3*x+5'


print(simpson13(n, a, b, f))
