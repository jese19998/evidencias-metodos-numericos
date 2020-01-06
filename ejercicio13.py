#Equipo Jese Manuel Acosta Avila y Gabriela Ramirez Cortez
#08/11/2019
#Ejercico 19

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Lista vacia
X=[]
Y=[]

#Leeyendo el archivo .csv
for line in open('data_2d.csv'):
    x1,x2,y=line.split(',')
    X.append([float(x1),float(x2)])
    Y.append([float(y)])

X=np.matrix(X)
y=np.array(Y)

#Graficar los puntos
flg=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.scatter(X[:,0],X[:,1],y)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')
plt.show()