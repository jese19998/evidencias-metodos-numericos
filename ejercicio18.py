#Equipo Jese Manuel Acosta Avila y Gabriela Ramirez Cortez
#21/11/2019
#Ejercicio 24 

import matplotlib.pyplot as plt
def funcion(x):
    return x**3-6*x**2+11*x-6


a=1.3
b=1.8
fa = funcion(a)
fb = funcion(b)

A=((b-a)*((fa+fb)/2.))
print(A)

plt.scatter(a,b)
plt.plot(x)
plt.show()
