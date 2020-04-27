#Author: Walter Nam
import numpy as np
from numpy import array, zeros, linalg, fabs

a = np.array([[1,-1,2,-1],[2,-2,3,-3],[1,1,1,0],[1,-1,4,3]], float)
b = np.array([-8, -20, -2, 4], float)

print("Solution of numpy")
print(np.linalg.solve(a,b))

n = len(b)
x = np.zeros(n, float)

#Elimination
for k in range(n - 1):
    if np.fabs(a[k,k]) < 1.0e-12:
        for i in range(k + 1, n):
            if np.fabs(a[i,k]) > np.fabs(a[k,k]):
                a[[k,i]] = a[[i,k]]
                b[[k,i]] = b[[i,k]]
    
    for i in range(k + 1, n):
        if a[i,k] == 0: continue
        factor = a[k,k] / a[i,k]
        for j in range(k,n):
            a[i,j] = a[k,j] - a[i,j] * factor
        b[i] = b[k] - b[i] * factor
print(a)
print(b)

#Backsubstitution
x[n - 1] = b[n - 1]/a[n-1, n-1]
for i in range (i + 1, n):
    sum_ax = 0
    for j in range(i + 1, n):
        sum_ax += a[i, j] * x[j]
    x[i] = (b[i] - sum_ax) / a[i,i]

print("Solution matrix")
print(x)