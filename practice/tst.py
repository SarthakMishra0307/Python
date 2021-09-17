import numpy as np
arr = np.array([2,4,6,7,1,3])

# sum = 0
# mean = 0
# diff_sqr =0

# for i in arr:
#     sum += i

# mean = sum/len(arr)
# print(mean)

# for i in arr:
#     diff_sqr += (i - mean)**2

# sdsq = diff_sqr/len(arr)

# sd = sdsq**(1/2)
# print(sd)

print(arr.std())

