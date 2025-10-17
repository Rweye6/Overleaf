import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
c = [] #A remplir
v = np.diff(c)/50
c = np.delete(c,len(c)-1,0)
#regression lineaire
a, b, r, p, err = stats.linregress(c,v)
print('Le modele affine v = a x c + b, a pour coefficients :\n a = ' + str(a) + '\n b = ' + str(b))
#Graphique
plt.scatter(c,v,marker = '+', color = 'blue')
plt.plot(c,a*c+b, color = 'red')
plt.xlabel('Cocncentration en (mol/L)')
plt.ylabel('Vitesse volumique de disparition en (mol/L/s)')
plt.title('Evolution de la vitesse en fonction de la concentration')
plt.show()
