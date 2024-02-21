import numpy as np
from numpy import random as R
import matplotlib.pyplot as plt

N = 10e6

rn = []
E = []
n = []
moment = 0.0
for i in range(1, int(N)+1):
    rn.append(R.rand())
    moment += rn[i-1]**3
    if i%1000 == 0:
        E.append(abs(moment/i-0.25)*np.sqrt(N))
        n.append(i)

fig = plt.figure(figsize=(7,5), dpi=140)
axes = fig.add_axes([0.15, 0.15, 0.75, 0.75])
axes.scatter(n, E, c='red', s=0.05)
axes.set_xlabel('$n_{i}$')
axes.set_ylabel('$\sqrt{N}\u03B5$')
axes.set_xlim(0.0, N)
axes.grid(lw=0.3)
plt.show()
    