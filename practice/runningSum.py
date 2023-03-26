nums = [3,1,2,10,1]
cont = 0
for i in range(len(nums)):
    cont += nums[i]
    nums[i] = cont
print(nums)