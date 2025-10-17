
import numpy as np
import matplotlib.pyplot as plt

Vb=np.arange(0,25+1)/1000
print (Vb)

##pH-métrie
pKa = 4.76
C1 = 0.0667
V1 = 0.02

Cb = 0.1

pH = np.arange(0,25+1)/1000
for i in range(26) :
    print(Vb[i])
    if (C1*V1-Cb*Vb[i]) >0 :
        pH[i] = 0.5*(pKa-np.log10((C1*V1-Cb*Vb[i])/(V1+Vb[i])))
    else :
        pH[i] = 14 + np.log10((Cb*Vb[i]-C1*V1)/(V1+Vb[i]))

plt.plot(Vb,pH)
plt.xlabel("Volume versé (L)")
plt.ylabel("pH")
plt.show()

##Conductimétrie
CMIHO = 19.8
CMIAcetate = 4.1
CMINa = 5.008
CMIH = 34.965

SIGMA = np.arange(0,25+1)/1000
for i in range(26) :
    print(Vb[i])
    if (C1*V1-Cb*Vb[i]) >0 :
        SIGMA[i] = CMINa*Cb*Vb[i]/(V1)+ CMIAcetate*Cb*Vb[i]/(V1) + CMIH*(C1*V1-Cb*Vb[i])/(V1)
    else :
        SIGMA[i] = CMINa*Cb*Vb[i]/(V1)+ CMIHO*(Cb*Vb[i]-C1*V1)/(V1) +  CMIAcetate*Cb*Vb[i]/(V1)

print(SIGMA)
plt.plot(Vb,SIGMA,'x')
plt.xlabel("Volume versé (L)")
plt.ylabel("$\sigma$ ($S.m^{⁻1}$)")
plt.xlim([0,0.025])
plt.ylim([0,3])
plt.show()
