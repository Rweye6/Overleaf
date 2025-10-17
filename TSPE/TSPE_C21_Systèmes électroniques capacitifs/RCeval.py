import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,7000,50)
y = -2.5*np.exp(-x/750)+2.5

plt.plot(x,y,'+',color='red')
plt.xlabel('$t$ (en s)')
plt.ylabel('$u_C$ (en V)')
plt.grid()
plt.show()
