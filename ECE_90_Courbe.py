import matplotlib.pyplot as plt
import pandas as pd

df =pd.read_csv('ECE_90.csv', sep = ';', decimal=',')

plot = df.plot.scatter(x='V', y = 'pH', title = "Titrage", colormap="viridis",ylim = (0,14), xlim = (0,20))
plt.show()

print(df.V)

V=list(df.V)
pH=[]

#for i in range(df.pH) :
    
plt.plot(df.V,df.pH,'+')
plt.ylim(0,14)
plt.xlim(0,20)

plt.show()
