#Author: Walter Nam
import sys
import pprint
import numpy as np 
import scipy as sp
from scipy import linalg


class Data:

    def __init__(self, A, b):
        self.A = A
        self.b = b

    def computed_sol(self, A, b):
        print("Numpy solution")
        try:
            return np.linalg.solve(A,b) 
        except np.linalg.LinAlgError:
            print("No solution")
            return None

    def gaussian(self, A, b):
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

        #Backward substitution
        x[n - 1] = b[n - 1] / A[n - 1, n - 1]
        for i in range(n - 2, -1, -1):
            sum_ax = 0
            for j in range(i + 1, n):
                sum_ax += A[i, j] * x[j]
            x[i] = (b[i] - sum_ax) / A[i,i] 

        return A, b, x

    def check_valid_solution(self, A, b, gauss):
        solution = gauss(A, b)[2]
        b_0 = gauss(A, b)[1]
        A_0 = gauss(A, b)[0]
        n = len(A_0)
        if np.isnan(np.sum(solution)):
            print("There are an infinite number of solutions")
            print("Solution with free variable = 1")
            return ""

        else:
            return solution
    
    def lu_decomp(self, A):
        (P, L, U) = sp.linalg.lu(A)
        print("L factor:")
        pprint.pprint(L)
        print("U factor:")
        pprint.pprint(U)
        return ""

A = np.array([
    [1,1,1],
    [2,2,1],
    [1,1,2]], 
    float)

b = np.array([4,6,6], float)
data = Data(A, b)
#print(data.computed_sol(A,b))
#print(data.gaussian(A, b))
#print(data.lu_decomp(A))
print(data.check_valid_solution(A, b, data.gaussian))