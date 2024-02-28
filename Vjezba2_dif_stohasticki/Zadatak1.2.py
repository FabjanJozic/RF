from numpy import random as R
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter

def setac(xy0, n):
    '''Funkcija random probabilistickog gibanja jedne cestice u 2D.
    \nxy0 ----- vektor pocetnih uvjeta
    \nn ------- broj iteracija'''
    kXY = np.zeros((3, int(n)+1))
    kXY[:, 0] = 0, xy0[0], xy0[1]
    for i in range(int(n)):
        kXY[0, i+1] = i
        r = R.rand()
        if r <= 0.1:
            kXY[1, i+1], kXY[2, i+1] = 0.05*kXY[1, i], 0.6*kXY[2, i]
        elif 0.1 < r and r <= 0.2:
            kXY[1, i+1], kXY[2, i+1] = 0.05*kXY[1, i], -0.5*kXY[2, i]+1.0
        elif 0.2 < r and r <= 0.4:
            kXY[1, i+1], kXY[2, i+1] = 0.46*kXY[1, i]-0.15*kXY[2, i], 0.39*kXY[1, i]+0.38*kXY[2, i]+0.6
        elif 0.4 < r and r <= 0.6:
            kXY[1, i+1], kXY[2, i+1] = 0.47*kXY[1, i]-0.15*kXY[2, i], 0.17*kXY[1, i]+0.42*kXY[2, i]+1.1
        elif 0.6 < r and r <= 0.8:
            kXY[1, i+1], kXY[2, i+1] = 0.43*kXY[1, i]+0.28*kXY[2, i], -0.25*kXY[1, i]+0.45*kXY[2, i]+1.0
        elif 0.8 < r and r <= 1.0:
            kXY[1, i+1], kXY[2, i+1] = 0.42*kXY[1, i]+0.26*kXY[2, i], -0.35*kXY[1, i]+0.31*kXY[2, i]+0.7
    return kXY

xy = [0.0, 0.0]
N = [100, 1e4]

[k, X, Y] = setac(xy, N[1])

'''fig = plt.figure(figsize=(6,5), dpi=120)
axes = fig.add_axes([0.15, 0.15, 0.80, 0.80])
plt.rcParams.update({'font.size': 8}) #type:ignore
axes.scatter(X, Y, label='{} koraka'.format(int(N[1])), s=0.1, color='purple')
#axes.grid(lw=0.4, linestyle=':')
axes.set_xlabel('$x$')
axes.set_ylabel('$y$')
axes.legend(loc='best')
plt.show()'''

fig = plt.figure(figsize=(10,7), dpi=120)
metadata = dict(title="Difuzija jedne cestice na stohasticki nacin")
writer = PillowWriter(fps=15, metadata=metadata) #type: ignore
with writer.saving(fig, "tree-sim.gif", 120):
    for j in range(len(X)):
        plt.clf()              
        #plt.plot(X[:j], Y[:j], color='red', lw=0.8)
        plt.scatter(X[j], Y[j], color='purple', s=0.1, label='{} koraka'.format(N[1]))
        plt.scatter(X[:j], Y[:j], color='purple', s=0.1)
        plt.axis('equal')
        #plt.grid(lw=0.4)
        plt.xlabel('$x$')
        plt.ylabel('$y$')
        plt.legend(loc='upper right')
        plt.xlim(min(X)-0.1, max(X)+0.1)
        plt.ylim(min(Y)-0.1, max(Y)+0.1)
        writer.grab_frame()