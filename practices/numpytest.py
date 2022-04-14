import numpy as np
m,n = eval(input())
arr = np.arange(0,m*n*2,2).reshape(m,n)
print(arr)