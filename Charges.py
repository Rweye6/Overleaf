import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-10, 10, 10)
y = np.linspace(-10, 10, 10)


qA = 10

qB = 20

A = (2,4)
B = (4,2)


#Tracé du champ vecteur champ électrostatique
for i in range(len(x)):
    for j in range(len(y)):
        dA = np.sqrt((x[i]-A[0])**2 + (y[j]-A[1])**2)
        dB = np.sqrt((x[i]-B[0])**2 + (y[j]-B[1])**2)
        
        FA = qA/dA
        FB = qB/dA
        
        alphaA = np.arccos((x[i]-A[0])/dA)
        alphaB = np.arccos((x[i]-B[0])/dB)

        print(i, j)
        plt.scatter(x[i], y[j],color = "black",marker="+")

        plt.arrow(x[i], y[j], FA*np.cos(alphaA), FA*np.sin(alphaA), head_width=0.1, head_length=0.1, fc='blue', ec='blue')
        plt.arrow(x[i], y[j], FB*np.cos(alphaB), FB*np.sin(alphaB), head_width=0.1, head_length=0.1, fc='red', ec='red')
       
plt.show()