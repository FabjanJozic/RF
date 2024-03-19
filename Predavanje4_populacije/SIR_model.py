import numpy as np
import matplotlib.pyplot as plt

#SIR model sirenja bolesti
N = 763
S = [N] #podlijezni bolesti
I = [1] #zarazeni
R = [0] #oporavljeni
gamma, beta = 0.5, 0.00218

def dRdt(s, i, r):
    return gamma*i
def dSdt(s, i, r):
    return -beta*i*s
def dIdt(s, i, r):
    return beta*s*i-gamma*i

T_total = 21
T = [0]
dt = 0.001
dS, dI, dR = [dSdt(S[0], I[0], R[0])], [dIdt(S[0], I[0], R[0])], [dRdt(S[0], I[0], R[0])]
while I[-1] > 0.0 and T[-1] <= T_total:
    T.append(T[-1]+dt)
    S.append(S[-1]+dS[-1]*dt), I.append(I[-1]+dI[-1]*dt), R.append(R[-1]+dR[-1]*dt)
    dS.append(dSdt(S[-1], I[-1], R[-1])), dI.append(dIdt(S[-1], I[-1], R[-1])), dR.append(dRdt(S[-1], I[-1], R[-1]))
    
fig = plt.figure(figsize=(8,5), dpi=120)
axes = fig.add_axes([0.10, 0.10, 0.85, 0.85])
plt.rcParams.update({'font.size': 8}) #type:ignore
axes.plot(T, S, label='S(t) - susceptibles', lw=1.6, color='black')
axes.plot(T, I, label='I(t) - infecteds', lw=1.6, color='blue')
axes.plot(T, R, label='R(t) - recovereds', lw=1.6, color='black', linestyle='--')
axes.grid(lw=0.4, linestyle=':')
axes.set_xlabel('$t$ / day')
axes.set_ylabel('population')
axes.set_xlim(0.0, T_total)
axes.legend(loc='best')
plt.show()
    