import numpy as np 
import matplotlib.pyplot as plt 
import difuzija as di
import sys

sys.getdefaultencoding()

def rho(x):
    if x >= 2.0 and x <= 5.0:
        return 5.5
    else:
        return 0.0

D = 1e-2

P1 = [0.0, 12.0, 0.0, 200.0, 1.00, 0.5] #pocetni uvjeti
P2 = [0.0, 12.0, 0.0, 200.0, 0.50, 0.5]
P3 = [0.0, 12.0, 0.0, 200.0, 0.20, 0.5]
P4 = [0.0, 12.0, 0.0, 200.0, 0.10, 0.5]
P5 = [0.0, 12.0, 0.0, 200.0, 0.05, 0.1]
P6 = [0.0, 12.0, 0.0, 200.0, 0.08, 0.1]
Rub = [0.0, 0.0] #rubni uvjeti
metoda = 'exp'

D1 = di.dif(rho, P1, Rub, D, metoda) #vrijednosti funkcije difuzije
D2 = di.dif(rho, P2, Rub, D, metoda)
D3 = di.dif(rho, P3, Rub, D, metoda)
D4 = di.dif(rho, P4, Rub, D, metoda)
D5 = di.dif(rho, P5, Rub, D, metoda)
D6 = di.dif(rho, P6, Rub, D, metoda)

X1 = [x for x in np.arange(0.0, 12.0+P1[4], P1[4])]
X2 = [x for x in np.arange(0.0, 12.0+P2[4], P2[4])]
X3 = [x for x in np.arange(0.0, 12.0+P3[4], P3[4])]
X4 = [x for x in np.arange(0.0, 12.0+P4[4], P4[4])]
X5 = [x for x in np.arange(0.0, 12.0+P5[4], P5[4])]
X6 = [x for x in np.arange(0.0, 12.0+P6[4], P6[4])]

fig = plt.figure(figsize=(7,6), dpi=120)
axes = fig.add_axes([0.10, 0.10, 0.85, 0.85])
plt.rcParams.update({'font.size': 8}) #type:ignore
axes.plot(X1, D1, label='$\u0394$t = {}s, $\u0394$x = {}m'.format(P1[5], P1[4]), lw=0.8, color='pink')
axes.plot(X2, D2, label='$\u0394$t = {}s, $\u0394$x = {}m'.format(P2[5], P2[4]), lw=1.1, color='red')
axes.plot(X3, D3, label='$\u0394$t = {}s, $\u0394$x = {}m'.format(P3[5], P3[4]), lw=1.4, color='red')
axes.plot(X4, D4, label='$\u0394$t = {}s, $\u0394$x = {}m'.format(P4[5], P4[4]), lw=0.8, color='darkred')
axes.plot(X5, D5, label='$\u0394$t = {}s, $\u0394$x = {}m'.format(P5[5], P5[4]), lw=1.4, color='cyan')
axes.plot(X6, D6, label='$\u0394$t = {}s, $\u0394$x = {}m'.format(P6[5], P6[4]), lw=1.1, color='purple')
axes.grid(lw=0.4, linestyle=':')
axes.set_xlabel('$x$ / m')
axes.set_ylabel('$\u03C1(x,t)$ / kgm$^{-1}$')
axes.set_xlim(0.0, 12.0)
#axes.set_ylim(0.0, 4.0)
axes.legend(loc='best')
axes.set_title('D = $10^{-2}$m$^{s}$s$^{-1}$, t = 200s')
plt.show()
