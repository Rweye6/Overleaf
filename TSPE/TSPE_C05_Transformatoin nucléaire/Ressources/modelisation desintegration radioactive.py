# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 14:14:59 2020

@author: Bodeme
"""

from random import randint as ri
import numpy as np
from scipy.optimize import curve_fit as cf
from pylab import *


def desintegrationRadioactive(n):
    noyaux = n * [1]
    nbNoyaux = [n]
    temps = [0]
    while len(noyaux)>0:
        for i in range(len(noyaux)):
            de = ri(1,6)
            if de == 6:
                noyaux[i] = 0
        nbNoyaux.append(sum(noyaux))
        noyaux = nbNoyaux[-1] * [1]
        temps.append(temps[-1]+1)
    #print(nbNoyaux)
    x = np.array(temps)
    y = np.array(nbNoyaux)
    reg = cf(lambda t,a,b: a*np.exp(b*t),x,y,p0=(x[0],-0.16))
    t12 = np.log(2)/abs(reg[0][1])
    #print(t12)
    figure(figsize=(10,6), dpi=80)
    subplot(1,1,1)
    plot(x,n*np.exp(x*reg[0][1]),'r:')
    scatter(x,y,marker='+',c='k')
    text(-temps[-1]/10,n,r'$N_0$',fontsize=14)
    annotate('',xy=(0,n), xytext=(-temps[-1]/40,n), arrowprops=dict(facecolor='black', arrowstyle='-'))
    text(-temps[-1]/20, n/2, r'$ \frac{N_0}{2} $',fontsize=14)
    annotate('',xy=(t12,n/2), xytext=(-temps[-1]/40,n/2), arrowprops=dict(facecolor='black', arrowstyle='-'))
    annotate('',xy=(t12,n/2), xytext=(t12,0), arrowprops=dict(facecolor='black', arrowstyle='<-'))
    text(t12-1,-n/10, r'$t_{1/2}$ = '+str(round(t12,1)),fontsize=14)
    grid(True)
    ax = gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))
    xlim(-temps[-1]/20,temps[-1])
    ylim(-n/20,21/20*n)
    title('Décroissance radioactive')
    xlabel('temps')
    ylabel('nombre de noyaux')
    savefig('DR.png')
    show()
