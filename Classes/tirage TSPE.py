import numpy as np
import matplotlib.pyplot as plt
import random
import csv
import pandas as pd


BASE = os.path.dirname(os.path.abspath(__file__))

df = pd.read_csv(os.path.join(BASE, "TSPE4.csv"), delimiter=";")

#Groupes 1 et 2
etu = list(df["Prenom"])
#groupe = list(df["Part"])
ligne = list()

random.shuffle(etu)
ligne.append("Les binomes sont : ")
for i in range(0,len(etu)) :
    if int(i/2) == i/2 and i != len(etu)-1 : ligne.append(etu[i] +" et " + etu[i+1])
    elif int(i/2) == i/2 and i == len(etu)-1 : ligne.append(etu[i])
    else : next

with open('Groupes_TP_TSPE4.txt', 'w') as fichier:
    fichier.write('\n'.join(map(str, ligne)))

import os  
os.system("pdflatex Groupes_Terminales.tex")
