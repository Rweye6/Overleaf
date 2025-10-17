import numpy as np
import matplotlib.pyplot as plt
import matplotlib


m=0.165
vm=120*1000/3600

d=12

F = (m*vm**2)/(2*d)

t = np.linspace(0,.8,num=13)

x = (.5*F*t**2)/m
y = [i*0 for i in t]

plt.plot(x,y,'x')
plt.tick_params(labelleft=False)
plt.show()
