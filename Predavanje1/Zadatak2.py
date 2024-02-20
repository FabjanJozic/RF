from numpy import random as R
import matplotlib.pyplot as plt

i = []
ri = []
for k in range(50000):
    i.append(k/1000)
    ri.append(R.rand())
    
fig = plt.figure(figsize=(7,5), dpi=140)
axes = fig.add_axes([0.15, 0.15, 0.75, 0.75])
axes.scatter(i, ri, c='magenta', s=0.05)
axes.set_ylabel('$r_{i}$')
axes.set_xlabel('$i$ / $10^{3}$')
axes.set_xlim(0.0, 50.0)
axes.set_ylim(0.0, 1.0)
plt.show()