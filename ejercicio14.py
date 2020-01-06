#Equipo Jese Manuel Acosta Avila y Gabriela Ramirez Cortez
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

#Lista vacia
X=[]
Y=[]

#Leeyendo el archivo .csv
data=open('data_2d.csv')
for linea in data:
    x1,x2,y=linea.split(',')
    X.append([float(x1),float(x2)])
    Y.append([float(y)])

X=np.matrix(X)
Y=np.array(Y)

#Graficar los puntos
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.scatter(X[:,1],X[:,2],Y)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')
plt.show()