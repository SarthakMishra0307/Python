nums = [4,1,2,1,2]
numset = {}
for i in nums:
    numset[i] = numset.get(i,0) + 1
print(nums[list(numset.values()).index(1)])
