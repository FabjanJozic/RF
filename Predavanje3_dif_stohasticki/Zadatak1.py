import numpy as np
from numpy import random as R
from scipy import stats as S
import matplotlib.pyplot as plt
import difuzija as di
import sys

sys.getdefaultencoding()

Nt, Nw = 200, 64000

squared = [0]
time = [0]
walkers = np.zeros((Nw, Nt+1))
for t in range(1, Nt+1):
    sumX = 0.0
    for w in range(Nw):
        d_x = (6*R.rand()-3)/100
        walkers[w, t] = walkers[w, t-1]+d_x
        sumX += (walkers[w, t])**2
    squared.append(sumX/Nw)
    time.append(t)

a, b, r, p, std_err = S.linregress(time, squared)

D = a/2
dx, dt = 0.005, 0.0001

P1 = [-1.0, 1.0, 0.0, 0.0, dx, dt] #pocetni uvjeti
P2 = [-1.0, 1.0, 0.0, 2.5, dx, dt]
P3 = [-1.0, 1.0, 0.0, 7.0, dx, dt]
P4 = [-1.0, 1.0, 0.0, 15.0, dx, dt]
P5 = [-1.0, 1.0, 0.0, 20.0, dx, dt]
Rub = [0.0, 0.0] #rubni uvjeti
metoda = 'exp'
def rho(x):
    if x >= -1.5*dx and x <= 1.5*dx:
        return 1.0
    else:
        return 0.0

D1 = di.dif(rho, P1, Rub, D, metoda) #vrijednosti funkcije difuzije
D2 = di.dif(rho, P2, Rub, D, metoda)
D3 = di.dif(rho, P3, Rub, D, metoda)
D4 = di.dif(rho, P4, Rub, D, metoda)
D5 = di.dif(rho, P5, Rub, D, metoda)

X1 = [x for x in np.arange(-1.0, 1.0+dx, dx)]
X2 = [x for x in np.arange(-1.0, 1.0+dx, dx)]
X3 = [x for x in np.arange(-1.0, 1.0+dx, dx)]
X4 = [x for x in np.arange(-1.0, 1.0+dx, dx)]
X5 = [x for x in np.arange(-1.0, 1.0+dx, dx)]

fig = plt.figure(figsize=(7,6), dpi=120)
axes = fig.add_axes([0.15, 0.15, 0.75, 0.80])
plt.rcParams.update({'font.size': 10}) #type:ignore
axes.plot(X1, D1, lw=1.0, color='orange')
axes.plot(X2, D2, lw=1.0, color='red')
axes.plot(X3, D3, lw=1.0, color='darkred')
axes.plot(X4, D4, lw=1.0, color='magenta')
axes.plot(X5, D5, lw=1.0, color='cyan')
axes.grid(lw=0.4, linestyle=':')
axes.set_xlabel('$x$ / m')
axes.set_ylabel('$\u03C1(x,t)$ / kgm$^{-1}$')
axes.set_xlim(-0.35, 0.35)
axes.set_ylim(-0.05, 1.05)
axes.legend(['t = {}s'.format(P1[3]), 't = {}s'.format(P2[3]), 't = {}s'.format(P3[3]),
             't = {}s'.format(P4[3]), 't = {}s'.format(P5[3])], loc='upper right')
axes.set_title('Diracova delta - difuzijska distribucija')
plt.show()