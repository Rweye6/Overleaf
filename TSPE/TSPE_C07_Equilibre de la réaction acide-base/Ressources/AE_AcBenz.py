import numpy as np
print("L'équation à résoudre est c_A*tau^2 + K_A*tau - K_A = 0")
c_A = float(input('c_A = '))
pK_A = float(input('pK_A = '))
K_A = 10**(-pK_A)
Delta = K_A**2 - 4*c_A*(-K_A)
if (Delta >0) :
    x_1 = (-K_A - np.sqrt(Delta))/(2*c_A)
    x_2 = (-K_A + np.sqrt(Delta))/(2*c_A)
    print("Deux solutions : tau_1 = " + str(x_1) + "et tau_2 = " + str(x_2))
elif (Delta==0) :
    x = -K_A/(2*c_A)
    print("Une solution double : tau = ",+str(x))
else :
    print("Aucune solution")
print("fin")

