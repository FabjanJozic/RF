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
dx, dt = 1e-4, 1.0

P1 = [-0.1, 0.1, 0.0, 0.0, dx, dt] #pocetni uvjeti
P2 = [-0.1, 0.1, 0.0, 10.0, dx, dt]
P3 = [-0.1, 0.1, 0.0, 80.0, dx, dt]
P4 = [-0.1, 0.1, 0.0, 100.0, dx, dt]
P5 = [-0.1, 0.1, 0.0, 150.0, dx, dt]
P6 = [-0.1, 0.1, 0.0, 200.0, dx, dt]
Rub = [0.0, 0.0] #rubni uvjeti
metoda = 'exp'
def rho(x):
    if x >= -dx and x <= dx:
        return 1.0
    else:
        return 0.0

D1 = di.dif(rho, P1, Rub, D, metoda) #vrijednosti funkcije difuzije
D2 = di.dif(rho, P2, Rub, D, metoda)
D3 = di.dif(rho, P3, Rub, D, metoda)
D4 = di.dif(rho, P4, Rub, D, metoda)
D5 = di.dif(rho, P5, Rub, D, metoda)
D6 = di.dif(rho, P6, Rub, D, metoda)

X1 = [x for x in np.arange(-0.1, 0.1+dx, dx)]
X2 = [x for x in np.arange(-0.1, 0.1+dx, dx)]
X3 = [x for x in np.arange(-0.1, 0.1+dx, dx)]
X4 = [x for x in np.arange(-0.1, 0.1+dx, dx)]
X5 = [x for x in np.arange(-0.1, 0.1+dx, dx)]
X6 = [x for x in np.arange(-0.1, 0.1+dx, dx)]

fig = plt.figure(figsize=(7,6), dpi=120)
axes = fig.add_axes([0.10, 0.10, 0.85, 0.85])
plt.rcParams.update({'font.size': 8}) #type:ignore
axes.plot(X1, D1, lw=0.8, color='pink')
axes.plot(X2, D2, lw=1.1, color='red')
axes.plot(X3, D3, lw=1.4, color='red')
axes.plot(X4, D4, lw=0.8, color='darkred')
axes.plot(X5, D5, lw=1.4, color='cyan')
axes.plot(X6, D6, lw=1.1, color='purple')
#axes.grid(lw=0.4, linestyle=':')
axes.set_xlabel('$x$ / m')
axes.set_ylabel('$\u03C1(x,t)$ / kgm$^{-1}$')
axes.set_xlim(-0.1, 0.1)
#axes.set_ylim(0.0, 4.0)
axes.legend(['t = {}s'.format(P1[3]), 't = {}s'.format(P2[3]), 't = {}s'.format(P2[3]),
             't = {}s'.format(P4[3]), 't = {}s'.format(P5[3]), 't = {}s'.format(P6[3]),],
            loc='upper right')
axes.legend(['D = {}'.format(D)], loc='upper left')
axes.grid(lw=0.2, linestyle=':')
plt.show()