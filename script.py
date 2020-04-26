#Author: Walter Nam
import numpy as np

#first gauss jordan to find the RREF

def gauss_jrdn(a, b):
    a = np.array(a, float)
    b = np.array(b, float)
    n = len(b)

    #main loop
    for k in range(n):
        #pivoting
        if np.fabs(a[k,k]) < 1.0e-12:
            for i in range(k + 1, n):
                if np.fabs(a[i, k]) > np.fabs(a[k, k]):
                    for j in range(k, n):
                        a[k, j], a[i, j] = a[i, j], a[k,j]
                    b[k], b[i] = b[i], b[k]
                    break
        #Division of the pivot row
        pivot = a[k, k]
        for j in range(k, n):
            a[k, j] /= pivot
        b[k] /= pivot
        #Elimination Loop
        for i in range(n):
            if i == k or a[i,k] == 0: continue
            factor = a[i,k]
            for j in range(k, n):
                a[i,j] -= factor * a[k, j]
            b[i] -= factor * b[k]
    return b,a

a = [[1,1,1], [2,2,1], [1,1,2]]
b = [4,6,6]

X,A = gauss_jrdn(a, b)
print(X)
print(A)