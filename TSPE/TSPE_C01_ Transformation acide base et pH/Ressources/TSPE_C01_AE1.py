## TP Definition du pH ##

import numpy as np
import matplotlib.pyplot as plt

# Points de mesure
c, pH = [...,...], [...,...] # A remplir avec les valeurs des mesures

# Trace du graphique en nuage de points
plt.xlabel('...') # A remplir
plt.ylabel('...') # A remplir
plt.title('...') # A remplir
plt.scatter(x=c, y=pH, marker='+', label='Mesures')
plt.legend()
plt.show()

#-------------------------------------

# Calcul du modele
cth = np.arange(1e-7, 0.1, 0.0001)
pHth = -np.log10(cth)

# Trace de la courbe modele
plt.plot(cth, pHth, color='red', label='Modelisation')