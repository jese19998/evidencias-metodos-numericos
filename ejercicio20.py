#Equipo Jese Manuel Acosta Avila y Gabriela Ramirez Cortez 
#22/11/2019
#Ejercicio 25 Resultados de las integrales

import matplotlib.pyplot as plt
from sympy import *
init_printing(use_unicode=False, wrap_line=False)
x=Symbol('x')

a=integrate(x**6,x)
b=integrate(x**1/2*1,x)
c=integrate(2*x**3-5*x**2-3*x+4,x)

print(a)
print(b)
print(c)

def funcion(x):
    return (3-4*x)/((3*x-x**2-2)**1/2)


a=-1
b=3
fa=funcion(a)
fb=funcion(b)

D=((b-a)*((fa+fb)/2.))
print(D)

plt.scatter(a,b)
plt.plot(x)
plt.show()
