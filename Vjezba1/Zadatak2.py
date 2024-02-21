from numpy import random as R
import numpy as np
import matplotlib.pyplot as plt

N = 3e5

E = []
X = []
Y = []
n = []
for i in range(1, int(N)):
    n.append(i)
    x, y = R.rand(), R.rand()
    if x**2+y**2 <= 1.0:
        X.append(x)
        Y.append(y)
    E.append(abs(4*len(X)/i-np.pi)*np.sqrt(N))
        
fig = plt.figure(figsize=(7,5), dpi=140)
axes = fig.add_axes([0.15, 0.15, 0.75, 0.75])
axes.scatter(n, E, c='red', s=0.02)
axes.set_xlabel('$n_{i}$')
axes.set_ylabel('$\sqrt{N}\u03B5$')
axes.set_xlim(0.0, N)
axes.grid(lw=0.3)
plt.show()

fig = plt.figure(figsize=(4,4), dpi=140)
axes = fig.add_axes([0.15, 0.15, 0.75, 0.75])
plt.axis('equal')
axes.scatter(X, Y, c='green', s=0.02)
axes.set_xlabel('$r = 1$')
axes.set_ylabel('$r = 1$')
axes.set_xlim(0.0, 1.0)
axes.set_ylim(0.0, 1.0)
axes.legend(['$x^{2} + y^{2} = r$'])
plt.show()
    