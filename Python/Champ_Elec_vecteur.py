import numpy as np
from matplotlib import pyplot as plt

m = 1000


x = np.linspace(10,100,6)
y = np.linspace(10,100,6)
g = list()
for i in x :
    for j in y :
        plt.scatter(i,j)
        g=((m/(np.sqrt(i**2 + j**2))))
        plt.arrow(i,j,-g,-g,head_width=2)
print(y)
#plt.plot(x,y)


plt.show()

print(g)
