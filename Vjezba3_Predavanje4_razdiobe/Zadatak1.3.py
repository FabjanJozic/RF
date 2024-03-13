import numpy as np
from numpy import random as R
from scipy import stats as S
import matplotlib.pyplot as plt
import difuzija as di
import sys
from matplotlib.animation import PillowWriter

sys.getdefaultencoding()

Nt, Nw = 200, 64000
dx, dt = 2.0, 0.1
X = [x for x in np.arange(-100.0, 100.0+dx, dx)]

squared = [0]
time = [0]
walkers = np.zeros((Nw, Nt+1))
Pi = np.zeros((len(X), Nt+1))
for t in range(1, Nt+1):
    sumX = 0.0
    for w in range(Nw):
        Dx = 6*R.rand()-3
        walkers[w, t] = walkers[w, t-1]+Dx
        sumX += (walkers[w, t])**2
        if walkers[w, t] >= -100.0 and walkers[w, t] <= 100.0:
            y = walkers[w, t]+100.0
            d = int(y/dx)
            Pi[d, t] += 1.0
    squared.append(sumX/Nw)
    time.append(t)
    
for p in range(len(X)):
    Pi[p, :] *= (1/dx)/(Nw) #normiranje funkcije vjerojatnosti setaca

a, b, r, p, std_err = S.linregress(time, squared)

Dif = a/2 #difuzijska konstanta, D = 1.5

P = [-100.0, 100.0, 0.0, 200.0, dx, dt] #pocetni uvjeti
Rub = [0.0, 0.0] #rubni uvjeti
metoda = 'exp'
def rho(x):
    if x > -0.9*dx and x < 0.9*dx:
        return 1/dx
    else:
        return 0.0

D = di.dif(rho, P, Rub, Dif, metoda) #vrijednosti funkcije difuzije

tekst = "slučajni hod: 64000 šetača, x$_{i}($t=0$)=0$\n\t$\u0394$x$\in$[-3, 3]cm, t=1s\ndifuzija: D=1.5cm$^{2}$s$^{-1}$, P$_{\u03C1}(x,0)$=$\u03B4(x=0)$ cm$^{-1}$\n\t$\u0394$x=2cm, $\u0394$t=0.1s"

#kod za gif
'''
fig = plt.figure(figsize=(10,7), dpi=120)
metadata = dict(title="Razdiobe")
plt.rcParams.update({'font.size': 15}) #type:ignore
writer = PillowWriter(fps=20, metadata=metadata) #type: ignore
with writer.saving(fig, "razdiobe_setaciVSdifuzija.gif", 120):
    for j in range(int(len(D)*dt)):
        plt.clf()
        plt.plot(X, Pi[:, j], lw=2.0, color='lightgreen', label='P$_{x}$ - šetač')
        plt.plot(X, D[int(j/dt)], lw=1.7, color='blue', label='P$_{\u03C1}$ - difuzija')
        #plt.axis('equal')
        #plt.grid(lw=0.4)
        plt.xlabel('$x$ / cm')
        plt.ylabel('P($x,t$) / cm$^{-1}$')
        plt.legend(loc='upper right')
        plt.xlim(-100.0, 100.0)
        plt.ylim(0.0, 0.05)
        plt.text(-98.0, 0.04, s=tekst, fontsize='medium')
        plt.text(24.0, 0.048, s='t={}s'.format(j), fontsize='medium')
        writer.grab_frame()
'''
  
#kod za fit i usporedbu
k = [70, 150, 400, 1000]

fig = plt.figure(figsize=(9,6), dpi=120)
axes = fig.add_axes([0.15, 0.15, 0.75, 0.80])
plt.rcParams.update({'font.size': 10}) #type:ignore
axes.plot(X, D[k[0]], lw=1.0, color='darkred', label='P$_{\u03C1}$, t = '+str(k[0])+'$\u0394$t')
axes.plot(X, Pi[:, int(k[0]*dt)], lw=1.2, color='darkred', linestyle=':', label='P$_{x}$, t = '+str(k[0])+'$\u0394$t')
axes.plot(X, D[k[1]], lw=1.0, color='red', label='P$_{\u03C1}$, t = '+str(k[1])+'$\u0394$t')
axes.plot(X, Pi[:, int(k[1]*dt)], lw=1.2, color='red', linestyle=':', label='P$_{x}$, t = '+str(k[1])+'$\u0394$t')
axes.plot(X, D[k[2]], lw=1.0, color='orange', label='P$_{\u03C1}$, t = '+str(k[2])+'$\u0394$t')
axes.plot(X, Pi[:, int(k[2]*dt)], lw=1.2, color='orange', linestyle=':', label='P$_{x}$, t = '+str(k[2])+'$\u0394$t')
axes.plot(X, D[k[3]], lw=1.0, color='lightgreen', label='P$_{\u03C1}$, t = '+str(k[3])+'$\u0394$t')
axes.plot(X, Pi[:, int(k[3]*dt)], lw=1.2, color='lightgreen', linestyle=':', label='P$_{x}$, t = '+str(k[3])+'$\u0394$t')
axes.grid(lw=0.4, linestyle=':')
axes.set_xlabel('$x$ / cm')
axes.set_ylabel('$\u03C1(x,t)$ / cm$^{-1}$')
axes.set_xlim(-100.0, 100.0)
axes.set_ylim(0.0, 0.1)
axes.legend(loc='upper right')
axes.set_title('Razdiobe')
plt.text(-98.0, 0.082, s=tekst, fontsize='medium')
plt.show()