import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

for i in range(len(arr)):
    print(arr[-i+1])