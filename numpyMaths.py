import numpy as np
arr1 = [[2, 27, 2, 21, 23],[2, 27, 2, 19, 23]]
arr2 = [2, 3, 4, 5, 6]
s=np.divide(arr1,arr2);
s=np.array([1]*len(arr1))
#print(s);
sm=np.zeros([len(arr1),len(arr1)])
for i in range(len(arr1)):
    for j in range(len(arr1)):
        sm[i][j]=1
print(sm)
#print("0 ")