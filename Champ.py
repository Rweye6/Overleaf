import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-10, 10, 15)
y = np.linspace(-10, 10, 15)

m = 10

T=(2,4)

#Tracé du champ vecteur champ gravitationnel
for i in range(len(x)):
    for j in range(len(y)):
        d = np.sqrt((x[i]-T[0])**2 + (y[j]-T[1])**2)
        G = - m / (d**2)
        print(G)
        alpha = np.arccos((x[i]-T[0])/d)
        print(i, j)
        plt.scatter(x[i], y[j],color = "black",marker="+")
        if y[j] < 0:
            alpha = -alpha
            plt.arrow(x[i], y[j], G*np.cos(alpha), G*np.sin(alpha), head_width=0.1, head_length=0.1, fc='blue', ec='blue')
        else:
            plt.arrow(x[i], y[j], G*np.cos(alpha), G*np.sin(alpha), head_width=0.1, head_length=0.1, fc='blue', ec='blue')

grav = np.linspace(-1,1,100)

for k in range(len(grav)):
    plt.plot(x, np.sqrt(m/grav[k] - (x-T[0])**2)+T[1])
    plt.plot(x, -np.sqrt(m/grav[k] - (x-T[0])**2)+T[1])

plt.show()