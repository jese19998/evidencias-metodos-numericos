#Equipo Jese Manuel Acosta Avila y Gabriela Ramirez Cortez
#11/10/2019
#Ejercicio 14

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
        
A=np.array([[-2.0,0.0,1.0],[-1.0,7.0,1.0],[5.0,-1.0,1.0]])
b=np.array([-4.0,-50.0,-26.0])

b=elimGauss(A,b)
print(A)
print(b)                
