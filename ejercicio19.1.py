#Equipo Jese Manuel Acosta Avila y Gabriela Ramirez Cortez
#22/11/2019
#Ejercicio 25 con las graficas

import matplotlib.pyplot as plt
from sympy import *
init_printing(use_unicode=False, wrap_line=False)
x=Symbol('x')

a=x**6,x
b=x**1/2*1,x
c=2*x**3-5*x**2-3*x+4,x

d=integrate(x**6,x)
e=integrate(x**1/2*1,x)
f=integrate(2*x**3-5*x**2-3*x+4,x)

print(d)
sp.plot(x**1/2*1,integrate(x**1/2*1,x))

print(e)
sp.plot(x**6,integrate(x**6,x))

print(f)
sp.plot(2*x**3-5*x**2-3*x+4,integrate(2*x**3-5*x**2-3*x+4,x))