import numpy as np
import matplotlib.pyplot as plt

#Création d'une variable temps, t, prenant 100 valeurs entre 0 et 0.1 secondes
t = np.linspace(0,0.1,100)
# Création de la grandeur amplitude
A1=float(input('Amplitude du dignal 1 : A1 = '))
# On fixe la fréquence du signal à 50 Hz
f = 50
# On fixe le déphasage phi à pi
phi=np.pi

####################################
# Définition d'une fonction sinusoïdale y1 d'après les paramètres au dessus
y1=A1*np.cos(2*np.pi*f*t+phi)

# Définition d'une fonction sinusoïdale y2 d'après les paramètres au dessus
y2=...

# Définition d'une fonction sinusoïdale y3 d'après les paramètres au dessus
y3=0

####################################
# Affichage de la fonction y1
plt.plot(t,y1,'-b',label="y1")
# Affichage de la fonction y2
plt.plot(t,y2,'-r',label="y2")
# Affichage de la fonction y3
#plt.plot(t,y3,'-m',label="y3")
# Ajout du titre
plt.title("Representation d'une fonction sinusoidale du temps")
# Ajout des titres des abscisses et des ordonnées
plt.xlabel('temps(s)')
plt.ylabel('amplitude')
# Affichage de la grille
plt.grid()
#Affichage de la légende
plt.legend()
#Affichage du graphique
plt.show()