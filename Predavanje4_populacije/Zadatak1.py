from numpy import random as R
import numpy as np

#radioaktivni raspad 
N = 12000
lam, dt, T = 0.529, 0.1, 10.0
for t in np.arange(dt, T+dt, dt):
    Nt = N
    for i in range(N):
        r = R.rand()
        if r <= lam*dt:
            Nt -= 1
    N = Nt
print(N)