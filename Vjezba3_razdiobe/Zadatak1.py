import numpy as np
from numpy import random as R
from scipy import stats as S
import matplotlib.pyplot as plt
import difuzija as di
import sys
from matplotlib.animation import PillowWriter

sys.getdefaultencoding()

Nt, Nw = 200, 64000

squared = [0]
time = [0]
walkers = np.zeros((Nw, Nt+1))
for t in range(1, Nt+1):
    sumX = 0.0
    for w in range(Nw):
        Dx = 6*R.rand()-3
        walkers[w, t] = walkers[w, t-1]+Dx
        sumX += (walkers[w, t])**2
    squared.append(sumX/Nw)
    time.append(t)

a, b, r, p, std_err = S.linregress(time, squared)

Dif = a/2
dx, dt = 2.0, 0.1

P = [-100.0, 100.0, 0.0, 200.0, dx, dt] #pocetni uvjeti
Rub = [0.0, 0.0] #rubni uvjeti
metoda = 'exp'
def rho(x):
    if x >= -dx and x <= dx:
        return 1/dx
    else:
        return 0.0

D = di.dif(rho, P, Rub, Dif, metoda) #vrijednosti funkcije difuzije

X = [x for x in np.arange(-100.0, 100.0+dx, dx)]

dx_s = 0.5 #dx setaca
Pi = np.zeros((int(200/dx_s)+1, 201))
Pi[:, 0] = 0.0, 0


tekst0 = "slučajni hod: 64000 šetača, x$_{i}($t=0$)=0$\n\t$\u0394$x$\in$[-3, 3]cm, t=1s\ndifuzija: D=1.5cm$^{2}$s$^{-1}$, P$_{\u03C1}(x,0)$=$\u03B4(x=0)$ cm$^{-1}$\n\t$\u0394$x=2cm, $\u0394$t=0.1s"

fig = plt.figure(figsize=(10,7), dpi=120)
metadata = dict(title="Razdiobe")
plt.rcParams.update({'font.size': 15}) #type:ignore
writer = PillowWriter(fps=40, metadata=metadata) #type: ignore
with writer.saving(fig, "razdiobe_setaciVSdifuzija.gif", 120):
    for j in range(int(len(D)*dt)):
        plt.clf()              
        plt.plot(X, D[int(j/dt)], lw=1.0, color='blue', label='P$_{\u03C1}$ - difuzija')
        #plt.axis('equal')
        #plt.grid(lw=0.4)
        plt.xlabel('$x$ / cm')
        plt.ylabel('P($x,t$) / cm$^{-1}$')
        plt.legend(loc='upper right')
        plt.xlim(-100.0, 100.0)
        plt.ylim(0.0, 0.05)
        plt.text(-98.0, 0.04, s=tekst0, fontsize='medium')
        plt.text(24.0, 0.048, s='t={}s'.format(j), fontsize='medium')
        writer.grab_frame()