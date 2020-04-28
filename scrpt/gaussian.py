#Author: Walter Nam
import sys
import pprint
import numpy as np 
import scipy as sp
import sympy
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

    def check_valid_solution(self, A, b, gauss, free_variable_solution):
        solution = gauss(A, b)[2]
        b_0 = gauss(A, b)[1]
        A_0 = gauss(A, b)[0]
        if np.isnan(solution[0]):
            print("There are an infinite number of solutions")
            print("Solution with free variable = 1")
            fv = 1
            free_variable_solution(A_0, b_0, fv, solution)
            print("Solution with free variable = -1")
            fv = -1
            free_variable_solution(A_0, b_0, fv, solution)
        elif np.isinf(solution[0]):
            print("No Solution")
        else:
            print(solution)
        
    def free_variable_solution(self, A_0, b_0, free_variable, solution_vector):
        x2 = free_variable
        x3 = solution_vector[len(solution_vector) - 1]
        x = sympy.symbols('x')
        expr = b_0[0] - A_0[0][0]*x - A_0[0][1]*x2  - A_0[0][2]*x3  
        x1 = sympy.solve(expr)
        print(np.array([x1[0], x2, x3], float))
    
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
    [1,1,2]
    ], 
    float)

b = np.array([4,4,6], float)
data = Data(A, b)
print(data.check_valid_solution(A, b, data.gaussian, data.free_variable_solution))
print(data.lu_decomp(A))