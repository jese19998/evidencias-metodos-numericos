#Equipo Jese Manuel Acosta Avila y Gabriela Ramirez Cortez
#21/11/2019
#Ejercicio 22 Integral definida

from sympy import *
init_printing(use_unicode=False, wrap_line=False)
x=Symbol('x')
a=integrate(x**3-6*x**2+11*x-6,(x,1.3,1.8))
print(a)