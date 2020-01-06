#Equipo Jese Manuel Acosta Avila y Gabriela Ramirez Cortez
import numpy as np 
def elimGauss(A,b):
    n = len(b)
    #face de eliminacion
    for k in range(0,n-1):
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a[i,k]/a[k,k]
                a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                b[i] = b[i]-lam*b[k]
    return a,b 
a = np.array([[4.0,-2.0,1.0],[-2.0,4.0,-2.0],[1.0,-2.0,1.0]])
b = np.array([[11.0],[-16.0],[17.0]])
a,b = elimGauss(a,b)
print(a)
print(b)