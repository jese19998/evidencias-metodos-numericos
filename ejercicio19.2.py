#Equipo Jese Manuel Acosta Avila y Gabriela Ramirez Cortez 
#22/11/2019
#Ejercicio 25 integral definida graficada

import matplotlib.pyplot as plt
def funcion(x):
    return (3-4*x)/((3*x-x**2-2)**1/2)


a=-1
b=3
fa=funcion(a)
fb=funcion(b)

A=((b-a)*((fa+fb)/2.))
print(A)
sp.plot(((3-4*x)/((3*x-x**2-2)**1/2)),(x,-1,3))