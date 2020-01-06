#Equipo Jese Manuel Acosta Avila y Gabriela Ramirez Cortez
#20/09/2019
#Ejercicio 4: Realizar un programaen el que el usuario introdusaca los 9 elementos de una matriz 3*3 y que el programa le debuelva al usuario si la matriz que inserto es singular o no.

import numpy as np
print('Introduce los 9 datos de tu matriz: ')
a11 = float(input('a11= '))
a12 = float(input('a12= '))
a13 = float(input('a13= '))
a21 = float(input('a21= '))
a22 = float(input('a22= '))
a23 = float(input('a23= '))
a31 = float(input('a31= '))
a32 = float(input('a32= '))
a33 = float(input('a33= '))

A = np.array([[a11,a12,a13],[a21,a22,a23],[a31,a32,a33]])
detA = np.linalg.det(A)
if np.round(detA,0) == 0.0:
    print('La matriz A es singular')
else: 
    print('la matriz A no es singular, es: %.2f' %detA )