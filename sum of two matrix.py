import numpy as np
arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
for e in range(3):
    for i in range(3):
        arr1[e][i]=arr1[e][i]+arr2[e][i]
print(arr1)
    