## TP Définition du pH ##

import numpy as np
import matplotlib.pyplot as plt

# Points de mesure
c, pH = [0.1,0.01,0.001,1*10**-4,1*10**-5,1*10**-6,1*10**-7], [1.1,2.1,3.3,3.9,4.9,6.1,6.9] # A remplir avec les valeurs des mesures

# Tracé du graphique en nuage de points
plt.xlabel('[$H_3O^+$]') # A remplir
plt.ylabel('pH') # A remplir
plt.title('Évolution du pH en fonction de la concentration en ions oxonium') # A remplir
plt.scatter(x=c, y=pH, marker='+', label='Mesures')
plt.legend()

# Calcul du modèle
cth = np.arange(1e-7, 0.1, 0.0001)
pHth = -np.log10(cth)

# Tracé de la courbe modèle
plt.plot(cth, pHth, color='red', label='Modélisation')

plt.show()

#------------------------------------------------------------------------


