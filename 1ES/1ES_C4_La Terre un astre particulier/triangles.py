import numpy as np

print("Calcul de l'angle BAC")
xb = float(input("Entrer xB : "))
yb = float(input("Entrer yB : "))


xa = float(input("Entrer xA : "))
ya = float(input("Entrer yA : "))


xc = float(input("Entrer xc : "))
yc = float(input("Entrer yc : "))

BAC = np.degrees(np.acos(((xc-xa)*(xb-xa)+(yc-ya)*(yb-ya))/(np.sqrt((xb-xa)**2+(yb-ya)**2)*np.sqrt((xc-xa)**2+(yc-ya)**2))))

AB = np.sqrt((xb-xa)**2+(yb-ya)**2)
print("L'angle BAC vaut :", BAC)
print("AB : ", AB)