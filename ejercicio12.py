#Equipo Jese Manuel Acosta Avila y Gabriela Ramirez Cortez
import numpy as np
import matplotlib.pyplot as plt

#creando lista vacia
X=[]
Y=[]

for linea in open('data_4d.csv'):
    x, y=linea.split(',')
    X.append(float(x))
    Y.append(float(y))
    
X=np.array(X)
Y=np.array(Y)

#Ecuaciones para obtener a y b
den=X.dot(X)-X.mean()*X.sum()
a=(X.dot(Y)-Y.mean()*X.sum())/den
b=(Y.mean()*X.dot(X)-X.mean()*X.dot(Y))/den

#Predicción
y_pred=a*X+b

#Graficando los datos
plt.title('Grafica de comparación de personas en USA anual del 2000 al 2010')
plt.scatter(X,Y)
plt.plot(X, y_pred, 'r')
plt.show()