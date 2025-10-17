import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,3,num=121)
y = np.sin(x)
z = 1.2*np.sin(x) + 0.6*np.sin(3.5*x)
#for i in (3,2,1,0,-1,-2,-3) :
#    y = i*np.sin(.5*x)
#    if i == 3 :
#        plt.plot(x,y,color="red")
#    else : plt.scatter(x,y,color="salmon",marker='.')

#plt.show()

#for i in (3,2,1,0,-1,-2,-3) :
#    y = i*np.sin(x)
#    if i == 3 :
#        plt.plot(x,y,color="blue")
#    else : plt.scatter(x,y,color="lightskyblue",marker='.')

#plt.show()

#z=1*np.sin(400*x)
#plt.plot(x,z,color="red")
#plt.show()


## Figure 2
intersec=[i for i in np.arange(0,3.5,0.5)]
ptjaune= [1.2*np.sin(i) + 0.6*np.sin(3.5*i) for i in intersec]

intersec2=[i for i in np.arange(0,3.25,0.25)]
ptrouge= [1.2*np.sin(i) + 0.6*np.sin(3.5*i) for i in intersec2]

fig, axs = plt.subplots(1,3)
#fig.suptitle('Vertically stacked subplots')

cap1="Signal analogique à échantillonner"
cap2="Des valeurs du signal analogique sont prélevées à intervalles de temps réguliers"
cap3="Un exemple d'échantillonnage avec une fréquence plus grande"

### Grids
axs[1].grid(axis = 'x')
for loc in intersec2 :
    axs[2].axvline(loc, alpha=1, color='#b0b0b0', linewidth=0.8)
for loc in intersec :
    axs[1].axvline(loc, alpha=1, color='#b0b0b0', linewidth=.8)

### Pour tous les graphs
for i in range(0,len(axs)) :
    ### reposition des axes à 0
    axs[i].spines["left"].set_position(("data", 0))
    axs[i].spines["bottom"].set_position(("data", 0))

    ### élimination des axes du haut et de droite
    axs[i].spines["top"].set_visible(False)
    axs[i].spines["right"].set_visible(False)

    ### transformation des traits des axes en fleches
    axs[i].plot(1, 0, ">k", transform=axs[i].get_yaxis_transform(), clip_on=False)
    axs[i].plot(0, 1, "^k", transform=axs[i].get_xaxis_transform(), clip_on=False)

    axs[i].set_xlabel("Temps")
    axs[i].set_ylabel("Amplitude")

    axs[i].set_xlim([0,3])
    axs[i].set_ylim([-.5,1.6])

    ### enlever les ticks des axes
    axs[i].set_xticks([])
    axs[i].set_yticks([])
    

axs[0].set_xlim([0,3])
axs[1].set_xlim([0,3])
axs[2].set_xlim([0,3])
axs[0].set_xticks([])
axs[0].set_yticks([])

axs[0].set_ylim([-.5,1.6])
axs[1].set_ylim([-.5,1.6])
axs[2].set_ylim([-.5,1.6])
#axs.ylim(0,3)
axs[0].plot(x, z)
axs[0].text(1.5, -.7, cap1, horizontalalignment='center',va='bottom')
axs[1].scatter(intersec,ptjaune)
axs[1].plot(x, z)
axs[1].text(1.5, -.7, cap2, horizontalalignment='center',va='bottom')
axs[2].scatter(intersec2,ptrouge)
axs[2].plot(x, z)
axs[2].text(1.5, -.7, cap3, horizontalalignment='center',va='bottom')


plt.show()


### Figure 3

intersec3=[i for i in np.arange(0,3.25,0.125)]
ptbleu= [1.2*np.sin(i) + 0.6*np.sin(3.5*i) for i in intersec3]

fig, axs = plt.subplots(1,3)
#fig.suptitle('Vertically stacked subplots')

cap1="Signal analogique à échantillonner"
cap2="Les valeurs du signal sont quantifiés sur 2 bits, soit 4 valeurs possibles."
cap3="Un exemple de quantification sur 3 bits"


for i in range(0,len(axs)) :
    ### reposition des axes à 0
    axs[i].spines["left"].set_position(("data", 0))
    axs[i].spines["bottom"].set_position(("data", 0))

    ### élimination des axes du haut et de droite
    axs[i].spines["top"].set_visible(False)
    axs[i].spines["right"].set_visible(False)

    ### transformation des traits des axes en fleches
    axs[i].plot(1, 0, ">k", transform=axs[i].get_yaxis_transform(), clip_on=False)
    axs[i].plot(0, 1, "^k", transform=axs[i].get_xaxis_transform(), clip_on=False)

    axs[i].set_xlabel("Temps")
    axs[i].set_ylabel("Amplitude")

    axs[i].set_xlim([0,3])
    axs[i].set_ylim([-.5,1.6])

    ### enlever les ticks des axes
    axs[i].set_xticks([])
    #axs[i].set_yticks([])

axs[0].plot(x, z)
axs[0].text(1.5, -.7, cap1, horizontalalignment='center',va='bottom')

### Calculs pour l'échantillonnage 2 bits
twobit=[]
B=[]
for i in intersec3[:-1] :
    B=list(x).index(i)
    if z[B]<.375 :
        twobit.append(0)
    elif z[B]<.75 :
        twobit.append(.375)
    elif z[B]<1.125 :
        twobit.append(.75)
    elif z[B]>1.125 :
        twobit.append(1.5)
    B=[]

axs[1].scatter(intersec3[:-1],twobit)
#axs[1].plot(x, z)
axs[1].plot(intersec3[:-1],twobit)
axs[1].text(1.5, -.7, cap2, horizontalalignment='center',va='bottom')

### Calculs pour l'échantillonnage 3 bits
threebit=[]
A=[]
B=[]

for i in intersec3[:-1] :
    B=list(x).index(i)
    if z[B]<1.5/2**3 :
        threebit.append(0)
    elif z[B]<2*(1.5/2**3) :
        threebit.append(1.5/2**3)
    elif z[B]<3*(1.5/2**3) :
        threebit.append(2*(1.5/2**3))
    elif z[B]<4*(1.5/2**3) :
        threebit.append(3*(1.5/2**3))
    elif z[B]<5*(1.5/2**3) :
        threebit.append(4*(1.5/2**3))
    elif z[B]<6*(1.5/2**3) :
        threebit.append(5*(1.5/2**3))
    elif z[B]<7*(1.5/2**3) :
        threebit.append(6*(1.5/2**3))
    elif z[B]<8*(1.5/2**3) :
        threebit.append(7*(1.5/2**3))
    elif z[B]>8*(1.5/2**3) :
        threebit.append(8*(1.5/2**3))
    
    
print(threebit)
axs[2].scatter(intersec3[:-1],threebit)
#axs[2].plot(x, z)
axs[2].plot(intersec3[:-1],threebit)
axs[2].text(1.5, -.7, cap3, horizontalalignment='center',va='bottom')

for loc in intersec3 :
    axs[0].axvline(loc, alpha=1, color='#b0b0b0', linewidth=0.8)
    axs[1].axvline(loc, alpha=1, color='#b0b0b0', linewidth=0.8)
    axs[2].axvline(loc, alpha=1, color='#b0b0b0', linewidth=0.8)

for loc in np.arange(0,2,(1.5/2**3)) :
    axs[2].axhline(loc, alpha=1, color='#b0b0b0', linewidth=0.8)
for loc in np.arange(0,2,(1.5/2**2)) :
    axs[1].axhline(loc, alpha=1, color='#b0b0b0', linewidth=0.8)
    #axs[1].axvline(loc, alpha=1, color='#b0b0b0', linewidth=0.8)
    #axs[2].axvline(loc, alpha=1, color='#b0b0b0', linewidth=0.8)
    
plt.show()

