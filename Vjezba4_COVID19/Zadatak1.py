import matplotlib.pyplot as plt

#modeliranje COVID-19 u Bugarskoj od 22.9.2020. do 15.2.2021.
S = [398664] #podlijezni bolesti
I = [5559] #zarazeni
R = [15777] #oporavljeni
gamma, beta = 0.016857, 1.90551e-7

Sw, Iw, Rw, Tw = [], [], [], [] #podaci sa interneta
with open('C:\\Users\\fabja\\Desktop\\programi\\RF\\Vjezba4_COVID19\\podaci_SIR.txt','r') as read:
    linija = read.readlines()
    for i in range(135):
        Sw.append(int(linija[i]))
        Iw.append(int(linija[i+135+1]))
        Rw.append(int(linija[i+2*(135+1)]))
        Tw.append(i)
    read.close()

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
    
fig = plt.figure(figsize=(9,5), dpi=120)
axes = fig.add_axes([0.15, 0.10, 0.80, 0.85])
plt.rcParams.update({'font.size': 8}) #type:ignore
axes.plot(T, S, label='S$_{sir}$', lw=1.6, color='brown')
axes.plot(T, I, label='I$_{sir}$', lw=1.6, color='blue')
axes.plot(T, R, label='R$_{sir}$', lw=1.6, color='red')
axes.scatter(Tw, Sw, label='S$_{web}$', color='white', edgecolor='brown', s=18)
axes.scatter(Tw, Iw, label='I$_{web}$', color='white', edgecolor='blue', s=18)
axes.scatter(Tw, Rw, label='R$_{web}$', color='white', edgecolor='red', s=18)
axes.grid(lw=0.4, linestyle=':')
axes.set_xlabel('$t$ / dan')
axes.set_ylabel('populacija')
axes.set_xlim(0.0, T_total)
axes.set_title('Modeliranje COVID-19 u Bugarskoj od 22.9.2020. do 15.2.2021.')
axes.legend(loc='best')
plt.show()
