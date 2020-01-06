#Equipo Jese Manuel Acosta Avila y Gabriela Ramirez Cortez
#25/10/2019
#Ejercicio 16

import numpy as np
import matplotlib.pyplot as plt

#Vamos a crear dos listas vacias

X = []
Y = []

#Vamos a leer los datos del archivo .csv (poner los archivos en la carpeta de trabajo)

for linea in open('data_1d.csv'):
    x,y =linea.split(',')
    X.append(float(x))
    Y.append(float(y))

#Convertit la lista a vectores
x = np.array(X)
y = np.array(Y)

#graficar los puntos
plt.scatter(X,Y)
plt.show()