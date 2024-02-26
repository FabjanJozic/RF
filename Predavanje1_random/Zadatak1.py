#linearna kongruentna metoda
a, c, M, r1 = 57, 1, 256, 10

ri = [0]*(M+10)
ri[0] = r1
for i in range(1, M+10):
    ri[i] = (a*ri[i-1]+c)%M
    
print(ri)
    