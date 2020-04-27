#Author: Walter Nam
import numpy as np

a = np.array([1,-1,2,-1],[2,-2,3,-3],[1,1,1,0],[1,-1,4,3], float)
b = np.array([-8, -20, -2, 4], float)
n = len(b)
x = np.zeros(n, float)

#Elimination
for k in range(n - 1):
