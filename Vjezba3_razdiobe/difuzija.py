import numpy as np

def Thomas(lower_diag, main_diag, upper_diag, solutions):
    '''Thomasova metoda za pronalazenje rjesenja linearnog sustava jednadzbi
    iz trodijagonalne matrice.'''
    a = lower_diag
    b = main_diag
    c = upper_diag
    d = solutions
    n = len(d)
    c_trenutno = [0]*n
    d_trenutno = [0]*n
    rez = [0]*n
    c_trenutno[0] = c[0]/b[0]
    d_trenutno[0] = d[0]/b[0]
    for i in range(1, n-1):
        c_trenutno[i] = c[i]/(b[i]-a[i-1]*c_trenutno[i-1])
        d_trenutno[i] = (d[i]-a[i-1]*d_trenutno[i-1])/(b[i]-a[i-1]*c_trenutno[i-1])
    d_trenutno[n-1] = (d[n-1]-a[n-2]*d_trenutno[n-2])/(b[n-1]-a[n-2]*c_trenutno[n-2])
    rez[n-1] = d_trenutno[n-1]
    for j in range(n-2, -1, -1):
        rez[j] = d_trenutno[j]-c_trenutno[j]*rez[j+1]
    return rez

def dif(g_x, xt0_N, R, D, met):
    '''Eksplicitna i implicitna metoda rjesavanje difuzijske parcijalne
    diferencijalne jednadzbe u 1D.
    \ng_x ------ funkcija pocetnih uvjeta za x varijablu
    \nxt0_N ---- vektor pocetnih uvjeta - [x0, xN, t0, tN, dx, dt]
    \nR -------- vektor rubnih uvjeta - [x<, x>]
    \nD -------- konstanta difuzije
    \nmet ------ metoda rjesavanja - "exp" / "imp"'''
    dx = xt0_N[4] #korak polozaja
    dt = xt0_N[5] #korak vremena
    N = int((xt0_N[1]-xt0_N[0])/dx) #broj tocaka u prostoru
    M = int((xt0_N[3]-xt0_N[2])/dt) #broj tocaka u vremenu
    dL = R[0] #lijevi rubni uvjet
    dD = R[1] #desni rubni uvjet
    alpha = D*dt/(dx**2)
    dif_p = np.zeros(N+1)
    dif_r = np.zeros(N+1)
    dif_L = []
    for u in range(len(dif_p)):
        dif_p[u] = g_x(xt0_N[0]+u*dx)
        if (dif_p[u] == 0.0 and dif_p[u-1] == 1/dx):
            U = dif_p[u-1]
            dif_p[u-1] = U/2
        elif (dif_p[u] == 1/dx and dif_p[u-1] == 0.0):
            U = dif_p[u]
            dif_p[u] = U/2
    dif_L.append(dif_p)
    if met == 'exp': #eksplicitna metoda
        for j in range(M+1): #vrijeme
            for i in range(1, N): #polozaj
                dif_r[i] = alpha*dif_p[i+1]+(1-2*alpha)*dif_p[i]+alpha*dif_p[i-1]
            dif_r[0], dif_r[-1] = dL, dD
            dif_p = np.copy(dif_r)
            dif_L.append(dif_p)
    elif met == 'imp': #implicitna metoda
        down = [-alpha]*N
        mid = [1+2*alpha]*(N+1)
        up = [-alpha]*N
        for j in range(M+1): #vrijeme
            dif_r = Thomas(down, mid, up, dif_p)
            dif_r[0], dif_r[-1] = dL, dD
            dif_p = np.copy(dif_r)
            dif_L.append(dif_p)
    else:
        print('Invalid method input.')
    return dif_L


        



            