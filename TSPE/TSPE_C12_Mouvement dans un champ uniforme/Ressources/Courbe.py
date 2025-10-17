import numpy as np
import matplotlib.pyplot as plt

g = 9.81 #m/s^2
v0 = 30 #m/s
h = 3 #m
alpha = 40*np.pi/180 #rad
t = np.linspace(0, 2*v0*np.sin(alpha)/g, 30)

xt =[]
yt = []
zt = []

for i in range (len(t)):
    xt.append(0)
    yt.append(0)
    zt.append(-0.5*g*t[i]**2 + v0*t[i] + h)
plt.plot(t,zt,"x",color="black")
plt.show()

# Trajectoire
x = np.linspace(0, 100, 30)
zx = []
for i in range (len(t)):
    zx.append(-0.5*g*(x[i]/(v0*np.cos(alpha)))**2 + np.tan(alpha)*x[i] + h)
plt.plot(x,zx,"x",color="black")


#Forces
m = 4 #kg
P=m*g
color = []
for i in range (len(t)):
    color.append("red")
plt.quiver(x,zx,0,-P)
plt.show()


#Vitesses
vx = []
vz = []
for i in range (len(t)):
    vx.append(v0*np.cos(alpha))
    vz.append(-g*t[i] + v0*np.sin(alpha))
plt.quiver(x,zx,vx,vz)
plt.show()
