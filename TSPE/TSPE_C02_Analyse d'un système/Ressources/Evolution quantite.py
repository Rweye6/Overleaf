"""
Programme permettant de représenter l'évolution des quantités de matière
des espèces du milieu réactionnel en fonction du volume de solution titrante versé
lors du titrage d'une solution d'acide éthanoïque par de la soude.
"""
"""
Réaction support du titrage de type A+B->C+D
A : réactif titré (acide éthanoïque) - cA = ? , VA
B : réactif titrant (ions hydroxyde) - cB , VE
C : produit (ions éthanoates)
D : produit (eau) > en excès donc non étudié
En présence d'espèces spectatrices :
AA : apportée par le réactif titré (eau) > en excès donc non étudié
BB : apportée par le réactif titrant (ions sodium)
"""

# Import du module pyplot de matplotlib en le renommant plt et de la bibliothèque numpy en la renommant np
import numpy as np
import matplotlib.pyplot as plt


# Saisie des données
VA=float(input("Volume initial du réactif titré en mL : VA = "))
cB=float(input("Concentration du réactif titrant en mol/L : cB = "))
VE=float(input("Volume de titrant versé à l'équivalence en mL : VE = "))


# Calcul, puis affichage de la concentration cA en réactif titré à partir de la relation à l'équivalence
cA=cB*VE/VA
print("La concentration en réactif titré est cA =",cA, "mol/L")


# Définition des grandeurs évoluant au cours du titrage

  # Abscisse :
VB = np.arange(0, 25, 0.1) # Construction d'un tableau avec des valeurs de VB tous les 0,1 entre 0 et 25

  # Ordonnée :
    # Initialisation des quantités de matière (Dans un premier temps, les quantités de matière sont indiquées égale à 0 pour toutes les valeurs de VB.)
nA = np.zeros(len (VB))
nB = np.zeros(len (VB))
nC = np.zeros(len (VB))
nBB = np.zeros(len (VB))
    # Calculs des valeurs des quantités de matière en fonction du volume VB versé
for i in range (len (VB)) :
   if VB[i] <= VE :
      nA[i] = cA*VA - cB*VB[i]
      nB[i] = 0
      nC[i] = cB*VB[i]
      nBB[i] = cB*VB[i]
   else :
      nA[i] =       ## COMPLETER
      nB[i] =       ## COMPLETER
      nC[i] =       ## COMPLETER
      nBB[i] =      ## COMPLETER


# Tracé de la courbe
plt.rcParams["figure.figsize"] = (8,8)  # dimensions du graphique
plt.plot(VB, nA, "-", label ='...') ## COMPLETER
plt.plot(VB, nB, "-", label ='...') ## COMPLETER
plt.plot(VB, nC, "-", label = '...') ## COMPLETER
plt.plot(VB, nBB, "-", label = '...') ## COMPLETER
plt.legend()
plt.title("...") ## COMPLETER
plt.xlabel("...") ## COMPLETER
plt.ylabel("...") ## COMPLETER
plt.grid()
plt.show()
