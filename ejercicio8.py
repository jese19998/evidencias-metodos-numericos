#Equipo Jese Manuel Acosta Avila y Gabriela Ramirez Cortez
#11/10/2019
#Ejercicio 15

#fase de eliminacion
import numpy as np
def elimGauss(a,b):
    n=len(b)
    for k in range(0,n-1):
        for i in range(k+1,n): 
            if a[i,k] != 0.0: 
                lam=a[i,k]/a[k,k]
                a[i,k+1:n]=a[i,k+1:n]-lam*a[k,k+1:n]
                b[i]=b[i]-lam*b[k]

# fase de eliminacion hacia atras
    for k in range(n-1,-1,-1):
        b[k] = (b[k] - np.dot(a[k,k+1:n],b[k+1:n])) /a[k,k]
        return b               
        
print('Introduce el sistema de ecuaciones: ')
a11 = float(input('a11= '))
a12 = float(input('a12= '))
a13 = float(input('a13= '))
a21 = float(input('a21= '))
a22 = float(input('a22= '))
a23 = float(input('a23= '))
a31 = float(input('a31= '))
a32 = float(input('a32= '))
a33 = float(input('a33= '))
A=np.array([[a11,a12,a13],[a21,a22,a23],[a31,a32,a33]])
print('Introduce los resultados del sistema: ')
b11 = float(input('b11= '))
b12 = float(input('b12= '))
b13 = float(input('b13= '))
b=np.array([[b11],[b12],[b13]])

detA = np.linalg.det(A)
if np.round(detA,0) == 0.0:
    print('No tiene solucon, la determinante es 0')
else: 
    print('Si tiene solución por que su determinante, es: %.2f' %detA )
    b=elimGauss(A,b)
    print(A)
    print(b)                
