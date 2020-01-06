#Equipo Jese Manuel Acosta Avila y Gabriela Ramirez Cortez
#26/09/2019
#Ejercicio 5

import numpy as np
L = np.array([[1,0,0],[2,3,0],[4,5,6]])
c = np.array([[1],[2],[3]])
def calcula_x(c,L):
    x1 = c[0]/L[0,0]
    x2 = (c[1]-(L[1,0]*x1))/L[1,1]
    x3 = c[2]-(L[2,0]*x1)-(L[2,1]*(x2))/L[2,2]
    return x1,x2,x3

print (x1)
print (x2)
print (x3)