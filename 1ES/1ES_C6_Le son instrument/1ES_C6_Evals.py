import numpy as np
import matplotlib.pyplot as plt

f = 1000
x = np.linspace(0,.01,num=500)
y = np.sin(f*2*np.pi*x)
z = 1.2*np.sin(x) + 0.6*np.sin(3.5*x)

plt.plot(x,y)
plt.grid()
plt.xlabel('temps (s)')
plt.ylabel('amplitude (V)')
plt.show()

