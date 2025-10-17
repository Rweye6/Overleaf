import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

t = [0,1,2,3,4,5,6,7,8,9]
A = [1.89, 1.79, 1.68, 1.58, 1.48, 1.38, 1.28, 1.17, 1.07, 0.97]
C=[]

for i in range(len(t)) :
    C.append(2.63E-5 * A[i])

plt.plot(t,C)
#plt.show()

print(C)

#regression lineaire
a, b, r, p, err = stats.linregress(t,C)
print('Le modele affine t = a x c + b, a pour coefficients :\n a = ' + str(a) + '\n b = ' + str(b))

