import numpy as np
import matplotlib.pyplot as plt

#populacija grabezljivca i plijena
V = [100] #populacija vjeverica
S = [15] #populacija sokolova
r_v, d_sv, r_vs, d_s = 2.0, 0.02, 0.01, 1.06
T_total = 12
dt = 0.001

def dSdt(v, s): #promjena populacije sokolova
    return r_vs*v*s-d_s*s
def dVdt(v, s): #promjena populacije vjeverica
    return r_v*v-d_sv*s*v

T, dV, dS = [0], [dVdt(V[0], S[0])], [dSdt(V[0], S[0])]
while T[-1] <= T_total:
    T.append(T[-1]+dt)
    V.append(V[-1]+dV[-1]*dt)
    S.append(S[-1]+dS[-1]*dt)
    dV.append(dVdt(V[-1], S[-1]))
    dS.append(dSdt(V[-1], S[-1]))
    
fig = plt.figure(figsize=(8,5), dpi=120)
axes = fig.add_axes([0.10, 0.10, 0.85, 0.85])
plt.rcParams.update({'font.size': 8}) #type:ignore
axes.plot(T, S, label='S(t) - sokolovi', lw=1.5, color='gray')
axes.plot(T, V, label='V(t) - vjeverice', lw=1.5, color='brown')
axes.grid(lw=0.4, linestyle=':')
axes.set_xlabel('$t$ / mjesec')
axes.set_ylabel('populacija')
axes.set_xlim(0.0, T_total)
axes.legend(loc='upper right')
plt.show()