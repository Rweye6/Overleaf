import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sc

#valeurs experimentales
... = np.array([...,...,...,...]) #I en mA
... = np.array([...,...,...,...]) #U en V

#Representation d'un nuage de points
plt.plot(...,...,'o', color = 'green')

#Modelisation d'une courbe : lignes a completer a l'aide du Document 2
droite = sc.linregress(...,...)
coefficient = droite.slope
print("Coefficient directeur : ", coefficient)
origine = droite.intercept
print("Ordonnee a l'origine : ", origine)

#Trace de la droite de regression : lignes a completer a l'aide du Document 2
U_modele = ...*I+...
plt.plot(I, U_modele, color = 'red')

#Configuration de l'aspect du graphique : renommer les axes et le titre
plt.xlabel("...")
plt.ylabel("...")
plt.title("...")
plt.grid()

#Affichage
plt.show()
