import numpy as np
import matplotlib.pyplot as plt

#modeliranje COVID-19 u Bugarskoj od 22.9.2020. do 15.2.2021.
S = [398664] #podlijezni bolesti
I = [5559] #zarazeni
R = [15777] #oporavljeni
gamma, beta = 0.016857, 1.90551e-7

Sw, Iw, Rw = [], [], []
with open('podaci_SIR.txt','r') as read:
    linija = read.readlines()
    for i in range(135):
        Sw.append(linija[i])
    read.close()

print(Sw)
def dRdt(s, i, r):
    return gamma*i
def dSdt(s, i, r):
    return -beta*i*s
def dIdt(s, i, r):
    return beta*s*i-gamma*i

T_total = 135
T = [0]
dt = 0.001
dS, dI, dR = [dSdt(S[0], I[0], R[0])], [dIdt(S[0], I[0], R[0])], [dRdt(S[0], I[0], R[0])]
while T[-1] <= T_total:
    T.append(T[-1]+dt)
    S.append(S[-1]+dS[-1]*dt), I.append(I[-1]+dI[-1]*dt), R.append(R[-1]+dR[-1]*dt)
    dS.append(dSdt(S[-1], I[-1], R[-1])), dI.append(dIdt(S[-1], I[-1], R[-1])), dR.append(dRdt(S[-1], I[-1], R[-1]))