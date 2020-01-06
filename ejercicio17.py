#Equipo Jese Manuel Acosta Avila y Gabriela Ramirez Cortez 
#21/11/2019
#Ejercicio 22 Integral indefinida

from sympy import *
init_printing(use_unicode=False, wrap_line=False)
x=Symbol('x')
a=integrate(x**3-6*x**2+11*x-6,x)

print(a)
