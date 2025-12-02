import random
import pandas as pd
import os

BASE = os.path.abspath(os.path.dirname(__file__))

# Lecture CSV
df = pd.read_csv(os.path.join(BASE, "TSPE4.csv"), delimiter=";")
etu = list(df["Prenom"])
random.shuffle(etu)

# Création des binômes
binomes = []
for i in range(0, len(etu), 2):
    if i+1 < len(etu):
        binomes.append(f"{etu[i]} et {etu[i+1]}")
    else:
        binomes.append(f"{etu[i]}")

# Fichier TEX des binômes
binomes_tex_path = os.path.join(BASE, "binomes.tex")

with open(binomes_tex_path, "w", encoding="utf-8") as f:
    for p in binomes:
        f.write(f"\\item {p}\n")

print("✔ Fichier binomes.tex généré.")

# Compilation
texfile = os.path.join(BASE, "Groupes__Terminales.tex")
cmd = f'pdflatex -interaction=nonstopmode -output-directory="{BASE}" "{texfile}"'
os.system(cmd)

print("🎉 PDF généré :", BASE)
