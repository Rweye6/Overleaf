import numpy as np
import matplotlib.pyplot as plt
t = []
x = []
y = []
plt.xlabel('Coordonnees x')
plt.ylabel('Coordonnees y')
plt.title('Trajectoire de la Terre')
plt.scatter(x, y, marker = '+')
i = 1
while i < len(t)-1 :
	alpha = np.arctan2(y[i], x[i]) - np.arctan2(y[i-1], x[i-1])
	r0 = np.sqrt(x[i]**2 + y[i]**2)
	r1 = np.sqrt(x[i-1]**2 + y[i-1]**2)
	A = r0*r1*np.sin(alpha)/2
	plt.fill([x[i], x[i-1], 0], [y[i], y[i-1], 0], label='A = ' + "%.2e"%A + ' u.a.**2')
	i += 2
plt.legend(loc='center right')
plt.show()
