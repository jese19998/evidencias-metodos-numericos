#Equipo Jese Manuel Acosta Avila y Gabriela Ramirez Cortez
#Ejercico 27
#29-noviembre-2019

from sympy import * 
import numpy as np
import matplotlib.pyplot as plt

def funcion(x):
    return 2*x**3-5*x**2+3*x+5

n=float(input('Ingersa tu valor menor: '))
a=0
b=n

fa=funcion(a)
fb=funcion(b) 

A=(b-a)*((fa+fb)/2.0)

f = lambda x : 2**3+x**2+5
a = 0; b =100 ; N = 10
n = 5

x = np.linspace(a,b,N+1)
y = f(x)

X = np.linspace(a,b,n*N+1)
Y = f(X)

plt.plot(X,Y)

for i in range(N):
    xs = [x[i],x[i],x[i+1],x[i+1]]
    ys = [0,f(x[i]),f(x[i+1]),0]
    plt.fill(xs,ys,'c',edgecolor='b',alpha=0.2)

plt.title("trapezoide")
plt.show()

print(A)