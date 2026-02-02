list_M = [300, 400, 500, 600, 700]  # masses en grammes
list_v_200ms = [0.40, 0.34, 0.32, 0.31, 0.28]  # vitesses en m/s
list_v_500ms = [0.81, 0.68, 0.59, 0.56, 0.51]  # vitesses en m/s

list_Metm = [] # en kg
list_dv = []  # en m/s
list_dv_sur_dt = []  # en m/s**2

for i in range(0,len(list_M)):
    list_Metm.append()
    list_dv.append()
    list_dv_sur_dt.append()

print(list_Metm)
print(list_dv)
print(list_dv_sur_dt)