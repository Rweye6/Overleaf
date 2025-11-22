import numpy as np
import matplotlib.pyplot as plt
import random
import csv
import pandas as pd


df = pd.read_csv("2GT6.csv", delimiter =";")

#Groupes 1 et 2
etu = list(df["Prenom"])
groupe = list(df["Part"])
groupone = list()
grouptwo = list()
ligne = list()

for i in range(0,len(groupe)):
    if groupe[i] == 1 :
        groupone.append(etu[i])
    else : grouptwo.append(etu[i])


print(groupone)
print(grouptwo)

random.shuffle(groupone)
ligne.append("Les binomes Groupe 1 sont : ")
for i in range(0,len(groupone)) :
    if int(i/2) == i/2 and i != len(groupone)-1 : ligne.append(groupone[i] +" et " + groupone[i+1])
    elif int(i/2) == i/2 and i == len(groupone)-1 : ligne.append(groupone[i])
    else : next

random.shuffle(grouptwo)
ligne.append("\nLes binomes Groupe 2 sont : ")
for i in range(0,len(grouptwo)) :
    if int(i/2) == i/2 and i != len(grouptwo)-1 : ligne.append(grouptwo[i] + " et " + grouptwo[i+1])
    elif int(i/2) == i/2 and i == len(grouptwo)-1 : ligne.append(grouptwo[i])
    else : next


with open('Groupes_TP_2GT6.txt', 'w') as fichier:
    fichier.write('\n'.join(map(str, ligne)))


df = pd.read_csv("2GT9.csv", delimiter =";")

#Groupes 1 et 2
etu = list(df["Prenom"])
groupe = list(df["Part"])
groupone = list()
grouptwo = list()
ligne = list()

for i in range(0,len(groupe)):
    if groupe[i] == 1 :
        groupone.append(etu[i])
    else : grouptwo.append(etu[i])


print(groupone)
print(grouptwo)

random.shuffle(groupone)
ligne.append("Groupe 1 : ")
for i in range(0,len(groupone)) :
    if int(i/2) == i/2 and i != len(groupone)-1 : ligne.append(groupone[i] +" et " + groupone[i+1])
    elif int(i/2) == i/2 and i == len(groupone)-1 : ligne.append(groupone[i])
    else : next

random.shuffle(grouptwo)
ligne.append("\nGroupe 2 : ")
for i in range(0,len(grouptwo)) :
    if int(i/2) == i/2 and i != len(grouptwo)-1 : ligne.append(grouptwo[i] + " et " + grouptwo[i+1])
    elif int(i/2) == i/2 and i == len(grouptwo)-1 : ligne.append(grouptwo[i])
    else : next


with open('Groupes_TP_2GT9.txt', 'w') as fichier:
    fichier.write('\n'.join(map(str, ligne)))

import os  
os.system("pdflatex Groupes Seconde.tex")
