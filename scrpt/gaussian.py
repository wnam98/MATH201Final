#Author: Walter Nam
import sys
import numpy as np

class Data:
    def __init__(self, A, b):
        self.A = A
        self.b = b

    def computed_sol(self, A, b):
        print("Numpy solution")
        return np.linalg.solve(A,b)

    def gauss_jordan(self, A, b):
        n = len(b)
        x = np.zeros(n, float)
        for i in range (n-1):
            if np.fabs(A[i,i]) < sys.maxsize:
                for j in range(i+1, n):
                    if np.fabs(A[j,i]) > np.fabs(A[i,i]):
                        A[[i,j]] = A[[j,i]]
                        b[[i,j]] = b[[j,i]]
                        break
            for k in range (i+1, n):
                if A[k,i] == 0: continue
                factor = A[i,i] / A[k,i]
                for j in range(i,n):
                    A[k,j] = A[i,j] - A[k,j] * factor
                b[k] = b[i] - b[k] * factor
        print(A)
        print(b)

        #Backward substitution
        x[n - 1] = b[n - 1] / A[n - 1, n - 1]
        for i in range(n - 2, -1, -1):
            sum_ax = 0
            for j in range(i + 1, n):
                sum_ax += A[i, j] * x[j]
            x[i] = (b[i] - sum_ax) / A[i,i]
    
        print("Solution of the system")
        print(x)

A = np.array([
    [1, -1, 2,-1],
    [2,-2, 3, -3],
    [1, 1, 1, 0],
    [1, -1, 4, 3]], 
    float)

b = np.array([-8, -20, -2, 4], float)
data = Data(A, b)
print(data.computed_sol(A,b))
print(data.gauss_jordan(A, b))
