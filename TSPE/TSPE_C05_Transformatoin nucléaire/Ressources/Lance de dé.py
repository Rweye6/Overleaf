# programme de simulation de décroissance radioactive
# par le jet de dés

# importations de fonctions utiles
import matplotlib.pyplot as plt
# matplotlib inline
from random import randint

# fonction permettant de lancer la simulation pour un
# nombre n d'atomes
def simulation(n):
    # initialisation des données
    nombrelance = 0
    temps = [0]
    radioactifs = [n]

    # coeur du programme
    while n > 0:
            desintegration = 0
            for i in range(n):
                tirage = randint(1,6)
                if tirage == 6:
                    desintegration = desintegration + 1
            n = n - desintegration
            nombrelance = nombrelance + 1
            temps.append(nombrelance)
            radioactifs.append(n)

    # affichage
    plt.figure()
    plt.plot(temps, radioactifs)
    plt.grid()
    plt.xlabel("temps")
    plt.ylabel("nombre d'atomes radioactifs")
    plt.show()
    #plt.close()
