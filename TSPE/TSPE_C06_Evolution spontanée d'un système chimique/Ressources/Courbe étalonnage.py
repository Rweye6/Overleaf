import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

C = [.25e-3,0.5e-3,0.75e-3,1e-3]
A = [0.62,1.3,1.65,1.9]

lr = stats.linregress(C,A)
print(lr)

Creg = np.linspace(0, 1e-3, 30)
Areg = lr[0]*Creg+lr[1]

plt.xlabel("$[FeSCN^{2+}]$ $mol.L^{-1}$")
plt.ylabel("Absorbance")
plt.xlim(0,1.2e-3)
plt.ylim(0,2)
plt.plot(C,A,"x",color="black")
plt.plot(Creg,Areg,color="blue")
plt.grid(color="lightblue")
#plt.annotate(["$A = 1664 \times C + 0,34$"], (0, 2),color="blue")
plt.text(.6e-3, 1.1, r'$A = 1664 \times C + 0,34$',
            fontsize = 10, color ="blue")
plt.show()
 
